n,k = map(int,input().split())
ans = 0
if k==0:
    ans = n**2
else:
    for i in range(1,n+1):
        loop = n//i
        rem = n%i
        ans += loop*max(i-k,0) + max(rem-k+1,0)
print(ans)