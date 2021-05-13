n = int(input())
f = [[int(i) for i in input().split()] for _ in range(n)]
p = [[int(i) for i in input().split()] for _ in range(n)]
ans = -float("inf")
for x in range(1,1<<10):
    res = 0
    for i in range(n):
        cnt = 0
        for j in range(10):
            if x>>j&1 and f[i][j]: cnt += 1
        res += p[i][cnt]
    ans = max(ans,res)
print(ans)