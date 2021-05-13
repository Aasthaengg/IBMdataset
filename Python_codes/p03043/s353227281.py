n, k = map(int , input().split())
ans = 0
for i in range(1, n+1):
    now = i
    j = 0
    while now <= k-1:
        now *= 2
        j += 1
    res = n*pow(2,j)
    ans += 1/res
print(ans)