n,t = map(int,input().split())
a = list(map(int,input().split()))
p = 0
m = 10**9+7
ans = 0
for i in range(n):
    if p < a[i]-m:
        p = a[i]-m
        ans = 1
    elif p == a[i]-m:
        ans += 1
    m = min(m,a[i])
print(ans)
