import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    flag = False  # 積を正にできるか

    if N == K:
        ans = 1
        for a in A:
            ans *= a
            ans %= MOD
            
        print(ans % MOD)
        exit()


    if len(pos) > 0:
        flag = True
    else:
        if K % 2 == 0:
            flag = True

    ans = 1
    if not flag:
        # 積を正にできないとき
        # 絶対値の小さい方からK個とる
        A = sorted([abs(x) for x in A])
        for a in A[:K]:
            ans *= a
            ans %= MOD
        ans *= -1
    else:
        pos = sorted(pos)
        neg = sorted(neg, reverse=True)
        if K % 2 == 1:
            # Kが奇数の時
            # 一番大きい偶数を1つとる。
            ans *= pos.pop()
            ans %= MOD

        # pos, neg sort -> 2個ずつペア -> 降順sort -> 上から K//2 個とる
        pairs = []
        while len(pos) >= 2:
            x = pos.pop()
            x *= pos.pop()
            pairs.append(x)
        while len(neg) >= 2:
            x = neg.pop()
            x *= neg.pop()
            pairs.append(x)
        pairs = sorted(pairs, reverse=True)
        for p in pairs[: K // 2]:
            ans *= p
            ans %= MOD

    print(ans % MOD)

    
if __name__ == '__main__':
    main()
