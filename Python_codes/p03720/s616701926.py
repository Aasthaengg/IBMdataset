N, M = map(int, input().split())
a_and_b = [list(map(int, input().split())) for i in range(M)]
for i in range(N):
    ans = 0
    for j in range(M):
        ans += a_and_b[j].count(i+1)
    print(ans)