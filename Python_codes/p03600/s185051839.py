def resolve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for src in range(N-1):
        for dst in range(src+1, N):
            mintotal = float("inf")
            for trans in range(N):
                if trans == src or trans == dst:
                    continue
                mintotal = min(mintotal, A[src][trans] + A[trans][dst])
            if A[src][dst] > mintotal:
                print(-1)
                return
            if A[src][dst] < mintotal:
                ans += A[src][dst]
    print(ans)




if '__main__' == __name__:
    resolve()