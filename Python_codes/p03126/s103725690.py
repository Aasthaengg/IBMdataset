N, M = map(int, input().split())
ka = [list(map(int, input().split())) for i in range(N)]

l = []
for i in range(N):
    for j in ka[i][1:]:
        l.append(j)

ans = 0
for i in range(M):
    if l.count(i+1) == N:
        ans += 1

print(ans)
