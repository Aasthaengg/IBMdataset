n,m,c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    s = c
    a = list(map(int,input().split()))
    for j in range(m):
        s += b[j] * a[j]
    ans += s > 0
print(ans)
