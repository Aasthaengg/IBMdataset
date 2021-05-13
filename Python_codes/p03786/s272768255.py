n = int(input())
a = list(map(int,input().split()))
maxA = max(a)
now = 0
a.sort()
ans = 0
for i in range(n-1):
    now += a[i]
    if a[i+1] <= now*2:
        ans += 1
    else:
        ans = 0

ans += 1
print(ans)