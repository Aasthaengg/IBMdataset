
n = int(input())
x = [-1]*n
for i in range(n):
    x[i] = list(map(int, input().split()))

ans = [[0]*3 for i in range(n)]
ans[0] = x[0]

for k in range(1,n):
    for j in range(3):
        ans[k][j] = max(ans[k-1][(j+1)%3], ans[k-1][(j+2)%3]) + x[k][j]

print(max(ans[n-1]))
