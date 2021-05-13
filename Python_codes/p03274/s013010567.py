n , k  = map(int,input().split())
x = list(map(int,input().split()))
ans = 10**9 
for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    if l*r >= 0:
        ans = min(ans,max(abs(r),abs(l)))
    elif l*r < 0:
        ans = min(ans,r-l + min(abs(r),abs(l)))
print(ans)