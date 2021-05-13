n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    ans = [0]*n
    for j in range(n):
        ans[j] = t[j]
    p = px[i][0] - 1
    ans[p] = px[i][1]
    print(sum(ans))