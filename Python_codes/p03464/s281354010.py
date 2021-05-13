K = int(input())
A = list(map(int, input().split()))

def solve():
    if A[K - 1] != 2:
        print(-1)
        return;
    M = 2
    m = 2
    for i in range(K - 1, 0, -1):
        nM = (M + A[i] - 1) - (M + A[i] - 1) % A[i - 1]
        if m % A[i - 1] == 0:
            nm = m
        else:
            nm = m + A[i - 1] - m % A[i - 1]
        #print("nM =", nM, "nm =", nm)
        if nM < m or nm >= M + A[i]:
            print(-1)
            return;
        #print("nM =", nM, "nm =", nm)
        M, m = nM, nm
    M = M + A[0] - 1
    # m = m
    print(m, M)
solve()
