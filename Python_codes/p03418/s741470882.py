n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    loop = n//i
    rem = n%i
    ans += max(0,i-k) * loop + max(rem+1-k,0)
if k==0:
    ans -= n
print(ans)