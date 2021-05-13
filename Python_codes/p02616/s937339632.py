import sys

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7


def main():

    N, K = map(int, sys.stdin.readline().rstrip().split())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]

    P, M = [], []
    # A を非負、負で振り分ける
    for i in range(N):
        n = A[i]
        if n < 0:
            M.append(n)
        else:
            P.append(n)

    # 絶対値の大きい方から並べる
    P.sort(reverse=True)
    M.sort()
    n_p = len(P)
    n_m = len(M)
    # print(P, M)

    # 全部使う
    if K == N:
        ans = 1
        for a in A:
            ans = ans * a % MOD
        print(ans)
        return

    # 全部負の場合
    if n_p == 0:
        if K % 2 == 1:  # 奇数なら小さな方から取る
            ans = 1
            for i in range(K):
                ans = ans * M[-(i + 1)] % MOD
            print(ans)
            return
        else:
            ans = 1
            for i in range(K):
                ans = ans * M[i] % MOD
            print(ans)
            return

    i, j = 0, 0
    if K % 2 == 1:
        i += 1
    
    while K > 1:
        p, m = 0, 0
        if i + 1 < n_p:
            p = P[i] * P[i + 1]
        if j + 1 < n_m:
            m = M[j] * M[j + 1]
        if p >= m:
            i += 2
        else:
            j += 2
        K -= 2

    # print(i, j)
    ans = 1
    for u in range(i):
        ans = ans * P[u] % MOD
    for v in range(j):
        ans = ans * M[v] % MOD

    print(ans)


main()
