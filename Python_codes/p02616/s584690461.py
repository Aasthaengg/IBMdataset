#写経
#https://atcoder.jp/contests/abc173/submissions/15061788

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    MOD = 10 ** 9 + 7
    ans = 1

    if K % 2 == 1 and A[-1] < 0:
        for i in range(K):
            ans = ans * A[N - (i + 1)] % MOD

        print(ans)
        return

    l = 0
    r = N - 1
    if K % 2 == 1:
        ans = ans * A[r]
        r -= 1
    
    for _ in range(K // 2):
        ml = A[l] * A[l + 1]
        mr = A[r] * A[r - 1]
        if ml > mr:
            ans = ans * ml % MOD
            l += 2
        else:
            ans = ans * mr % MOD
            r -= 2

    print(ans)
    return
resolve()