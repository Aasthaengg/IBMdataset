def comb_mod(n,r,m):
    ans = 1
    for i in range(1,r+1):
        ans *= (n-i+1) % m
        ans *= pow(i,m-2,m) % m
        ans = ans % m
    return ans
x,y = map(int,input().split())
m = 10**9+7
n = (x+y)//3
c = 0
if x*0.5 <= y <= 2*x and (x+y)%3 == 0:
    r = x - n
    c = comb_mod(n,r,m)
else:
    ans = 0
print(c)
