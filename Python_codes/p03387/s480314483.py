a = sorted(list(map(int, input().split())))
ans = 0
if (a[0]%2==0 and a[1]%2==0) or (a[0]%2!=0 and a[1]%2!=0):
    ans = a[2]-a[1] + (a[2]-(a[0]+a[2]-a[1]))//2
else:
    ans = 1
    a[1] += 1
    a[2] += 1
    ans += (a[1]-a[0])//2 + a[2]-a[1]
print(ans)