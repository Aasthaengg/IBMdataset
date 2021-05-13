n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    if i-k > 0:
        ans += (n//i)*(i-k) 
        if (n%i) >= k:
            ans += (n%i) - k + 1
if k == 0:
    print(ans-n)
else:
    print(ans)