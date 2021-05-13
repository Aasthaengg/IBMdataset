n,m = map(int,input().split())
ans = 0
for i in range(1,n+1):
    ans += n // i * max(i-m,0) + max(n%i-m+1,0)
if m == 0:
    ans -= n
print(ans)