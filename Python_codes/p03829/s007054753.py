def abc052_d():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += min(B, A * (X[i] - X[i-1]))
    print(ans)

abc052_d()