n,k = map(int,input().split())
ans = 0
if k == 0:
    print(n**2)
    exit()
for i in range(k+1,n+1):
    ans += (i-k) * (n//i)
    ans += max(0,n%i-k+1)
print(ans)