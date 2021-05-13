n = int(input())
a = list(map(int,input().split()))
zougen = 2
ans = 0

for i in range(1,n):
    if i == n-1:
        if zougen == 2:
            ans += 1
        elif zougen == 0:
            if a[i]-a[i-1]<0:
                ans += 2
            else:
                ans += 1
        else:
            if a[i]-a[i-1] > 0:
                ans += 2
            else:
                ans += 1
    elif zougen == 2:
        if a[i]-a[i-1]>0:
            zougen = 0
        elif a[i]-a[i-1]<0:
            zougen = 1
        else:
            zougen = 2
    elif zougen == 0:
        if a[i]-a[i-1]<0:
            zougen = 2
            ans += 1
    elif zougen == 1:
        if a[i]-a[i-1]>0:
            zougen = 2
            ans += 1

if n == 1:
    ans = 1

print(ans)
