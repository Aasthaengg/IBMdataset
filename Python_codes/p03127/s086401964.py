def gcd(x,y):
    if x < y:
        x,y = y,x
    if x%y == 0:
        return y
        
    return gcd(y,x%y)

n=int(input())

a=list(map(int,input().split()))
ans=a[0]
for i in range(1,len(a)):
    ans = gcd(ans,a[i])
    
print(ans)    