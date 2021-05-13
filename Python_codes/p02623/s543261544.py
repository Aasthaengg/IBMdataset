def solve():
    N,M,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ai = 0
    bi = 0
    s = 0

    ans = 0
    for i, a in enumerate(A):
        if s + a > K:
            ai = i-1
            ans = i
            break
        s += a
    else:
        ans = len(A)
        ai = len(A)-1

    #print(ans, ai, s)
    while ai >= -1:
        while bi < len(B):
            if s + B[bi] > K:
                break
            s += B[bi]
            bi += 1
        ans = max(ans, ai+1+bi)
        if ai != -1:
            s -= A[ai]
        ai -= 1

    print(ans)

solve()