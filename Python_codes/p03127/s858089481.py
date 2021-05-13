n=int(input())
a=list(map(int,input().split()))

def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

ans=a[0]
for i in a:
    ans=gcd(ans,i)
print(ans)