import random

class RollingHash(object):
    def __init__(self, S: str, MOD: int = 998244353, BASE: int = 37):
        self.S = S
        self.N = N = len(S)
        self.MOD = MOD
        self.BASE = BASE
        self.S_arr = [ord(x) for x in S]

        self.POWER = [1] * (N + 1)
        self.HASH  = [0] * (N + 1)
        p, h = 1, 0
        for i in range(N):
            self.POWER[i + 1] = p = (p * BASE) % MOD
            self.HASH[i + 1] = h = (h * BASE + self.S_arr[i]) % MOD

    def hash(self, l: int, r: int):
        # get hash for S[l:r]
        _hash = (self.HASH[r] - self.HASH[l] * self.POWER[r - l]) % self.MOD
        return _hash

# 汎用的な二分探索のテンプレ
# check_func(x) = true となるxの最小値を探索する
# left : check_func(x) = falseとなるx
# right: check_func(x) = true となるx
# search_max: check_func(x) = true となるxの"最大値"を探索する場合はTrue
# check_func: search_max = False の場合、answer <= x であればcheck_func(x) = true となるような関数
#             search_max = True  の場合、x <= answer であればcheck_func(x) = true となるような関数
def binary_search(left: int, right: int, check_func, search_max:bool=False):
    # ok と ng のどちらが大きいかわからないことを考慮
    while abs(right - left) > 1:
        mid = (left + right) // 2
    
        if check_func(mid) ^ search_max:
            right = mid
        else:
            left = mid

    return left if search_max else right

def main():
    N = int(input())
    S = input()
    MOD = 10 ** 18 + 3
    # BASEはMOD未満で1でない奇数とする
    BASE = random.randint(2, MOD // 2 - 1) * 2 + 1
    rs = RollingHash(S, MOD=MOD, BASE=BASE)

    D = [0] * N
    # 長さLの部分文字列同士が、範囲を重ねず同じ文字列となる場合はTrue,
    # そうでない場合はFalseを返す関数
    def isOK(L):
        if L == 0:
            return True
        
        for i in range(min(L, N - 2 * L + 1)):
            D[i] = rs.hash(i, i + L)
        hashes = set()
        for i in range(L, N - L + 1):
            # 自分より開始点がL以上前の文字列のハッシュを検索対象に追加
            hashes.add(D[i - L])
            D[i] = v = rs.hash(i, i + L)
            # ハッシュが衝突したら、範囲を重ねず同じ文字列となる文字列が存在することになる
            if v in hashes:
                return True
        return False

    # 範囲が重ならないことが条件にあるので、答えは最大でもN // 2（文字列の長さの半分）となる。
    # ただし、二分探索する上で絶対に答えとならない範囲を含めたいので、
    # 探索範囲としてはN // 2 + 1 と、+1しておく。
    ans = binary_search(0, N // 2 + 1, isOK, search_max=True)
    print(ans)

if __name__ == '__main__':
    main()