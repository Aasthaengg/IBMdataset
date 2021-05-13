n, m, q = map(int, input().split())
start_goal = [[0]*n for _ in range(n)]
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    start_goal[l][r] += 1
#print(start_goal)

#2次元累積和
s_2 = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        s_2[i+1][j+1] = s_2[i][j+1] + s_2[i+1][j] - s_2[i][j] + start_goal[i][j]
#print(s_2)

for _ in range(q):
    l, r = map(int, input().split())
    ans = s_2[n][r] - s_2[l-1][r]
    print(ans)
