n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0

for i in range(n):
    if b[i] >= a[i]:
        ans += a[i]
        if max(0,(a[i+1]-(b[i]-a[i]))) == 0:
            ans += a[i+1]
            a[i+1] = 0
        else:
            ans += (b[i]-a[i])
            a[i+1] -= (b[i]-a[i])
    else:
        ans += b[i]
print(ans)