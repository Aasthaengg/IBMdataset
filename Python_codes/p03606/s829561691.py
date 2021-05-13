def resolve():
    N = int(input())
    lr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += lr[i][1] - lr[i][0] + 1
    print(ans)
resolve()