h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

mat_map = [()]*(h*w+1)

for i in range(h):
    for j in range(w):
        mat_map[a[i][j]] = (i, j)

dp = [0]*(h*w+1)

for i in range(h*w-1, 0, -1):
    if i+d > h*w:
        continue
    current = mat_map[i]
    nex = mat_map[i+d]
    dist = abs(current[0]-nex[0]) + abs(current[1]-nex[1])
    dp[i] = dp[i+d] + dist

q = int(input())
ans= []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(dp[l]-dp[r])

print(*ans, sep='\n')