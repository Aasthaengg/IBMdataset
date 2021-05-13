n = int(input())
a = list(map(int,input().split()))

a.sort()
mx = a[-1]

half = mx / 2
dist = abs(half - a[0])
ans = 0
for i in range(1,n):
    if dist > abs(half - a[i]):
        dist = min(dist,abs(half - a[i]))
        ans = a[i]
print(mx,ans)
