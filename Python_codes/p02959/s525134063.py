n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    if b[i]>=a[i]:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0
        c = min(b[i],a[i+1])
        ans += c
        b[i] -= c
        a[i+1] -= c
    else:
        ans += b[i]
        a[i] -= b[i]
        b[i] -= b[i]

print(ans)