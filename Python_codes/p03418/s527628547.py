n,k = map(int, input().split())
ans = 0
for b in range(k+1,n+1):
    r = n//b
    ans += (b-k)*r
    if (n-r*b-k + 1)>0:
        ans += (n - r*b - k + 1)

if k == 0:
    ans =n**2

print(ans)