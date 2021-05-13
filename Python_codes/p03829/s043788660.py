n,a,b = map(int,input().split())
x = list(map(int,input().split()))

ans = 0


for i in range(n-1):
    ps = x[i+1]-x[i]
    if ps*a >= b:
        ans +=b
    else:
        ans += ps*a
    
print(ans)
