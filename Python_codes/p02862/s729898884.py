def comb_mod(n,r,m):
    ans = 1
    for i in range(1,r+1):
        ans *= (n-i+1) % m
        ans *= pow(i,m-2,m) % m
        ans = ans % m
    return ans

x,y = map(int,input().split())
m = 10**9+7
if x > 2*y or 2*x < y or (x+y)%3 != 0:
    ans = 0
else:
    n = (x+y)//3
    r = x-n
    ans = comb_mod(n,r,m)
print(ans)