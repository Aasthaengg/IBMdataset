def e_max_gcd(N, K, A):
    def divisor_list(n):
        """n の正の約数のリスト"""
        ret = []
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                ret.append(k)
                if k != n // k:
                    ret.append(n // k)
        ret.sort()
        return ret

    ans = 1  # 任意の整数は1の倍数
    for c in divisor_list(sum(A)):  # sum(A)の約数が解の candidate
        r = sorted([a % c for a in A])
        # rをある位置で左右に分けたとき、「左」には-1、「右」には+1する操作を
        # 行って全要素をcの倍数にしたい。このとき、「左」の要素の和の分だけ
        # 操作してよいが、それはKを超えてはならない。
        # 最初、すべての要素を「左」に入れる。
        # 「左」の要素の関数値A(-1してcの倍数にするための操作回数)は最初sum(r)とし、
        # 「右」の要素の関数値B(+1してcの倍数にするための操作回数)は最初0とする。
        # ここで「左」の要素eを右から順に「右」に入れていくとすると、1つ入れるごとに
        # A の値は e だけ減り、B の値は c - e だけ増える。
        # よって A-B の値は1つ「右」に入れるごとに c だけ減る。
        # ゆえに、「右」に何個の要素を入れるべきかは sum(r)//c からわかる。
        if sum(r[:N - sum(r) // c]) <= K:
            ans = max(ans, c)
    return ans

N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(e_max_gcd(N, K, A))