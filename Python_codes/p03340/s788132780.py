n = int(input())
a = list(map(int, input().split()))

xor = 0
ans = 0

right = 0

for l in range(n):
    if l>0:
        xor -= a[l-1]
    for r in range(right,n):
        if xor^a[r] == xor+a[r]:
            if r==n-1:
                ans += r-l+1
                right = max(r,l+1)
            else:
                xor += a[r]
        else:
            ans += r-l
            right = max(r,l+1)
            break

print(ans)