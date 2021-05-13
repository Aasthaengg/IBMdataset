n, k = map(int, input().split())
a = list(map(int, input().split()))
grid = [[0,0] for x in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            grid[i][0]+=1
    for j in range(i, n):
        if a[j] < a[i]:
            grid[i][1]+=1

mod = 1000000007
ans = 0
for i in range(n):
    ans += k * (2*grid[i][1] + (k-1)*grid[i][1]) // 2
    ans %= mod
    ans += (k-1) * (2*grid[i][0] + (k-2)*grid[i][0]) // 2
    ans %= mod
print(ans)


            
