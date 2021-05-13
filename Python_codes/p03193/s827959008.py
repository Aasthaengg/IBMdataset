def resolve():
    N, H, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        if A[i] >= H and B[i] >= W:
            ans += 1
    print(ans)
resolve()