def resolve():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if abs(x[i]) <= abs(K-x[i]):
            ans += 2*abs(x[i])
        elif abs(x[i]) >= abs(K-x[i]):
            ans += 2*abs(K-x[i])
    print(ans)
resolve()