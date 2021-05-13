n = int(input())
dist = [list(map(int, input().split())) for i in range(n)]
use = [[True]*n for _ in range(n)]
# 最短性の確認
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                print(-1)
                exit()
            if (i - j) * (j - k) * (k - i) and dist[j][k] == dist[j][i] + dist[i][k]:
                use[j][k] = False
                
ans = 0

for i in range(n):
    for j in range(i+1, n):
        if use[i][j]:
            ans += dist[i][j]

print(ans)
