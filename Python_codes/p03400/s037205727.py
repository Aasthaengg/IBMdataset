def resolve():
    N = int(input())
    D, X = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        count = 1
        while count <= D:
            count += A[i]
            ans += 1
    print(ans+X)
resolve()