import math
def per(n,r):
    return math.factorial(n)//math.factorial(n-r)

n,k=map(int,input().split())

if k%2==0:
    #偶数の時
    amari1=n//k
    amari2=n//(k-k//2)-amari1
    ans=amari1**3+amari2**3
else:
    amari=n//k
    ans=amari**3
print(ans)