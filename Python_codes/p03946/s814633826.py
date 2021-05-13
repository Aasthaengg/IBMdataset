n , t = map(int,input().split())
a = list(map(int,input().split()))
k = [0 for i in range(n)]
nowmin = a[0]
for i in range(1,n):
    k[i] = a[i] - nowmin
    nowmin = min(nowmin,a[i])

maxri = max(k)
ans = 0
for i in range(n):
    if k[i] == maxri:
        ans += 1
print(ans)