n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(m)]
ans = [[] for i in range(n)]
for i in range(n):
    for j in range(m):
        ans[i].append(abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1]))
for i in range(n):
    print(ans[i].index(min(ans[i]))+1)