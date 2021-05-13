from math import gcd as g
n=int(input())
t=[]
for i in range(n):
    t.append(int(input()))
def l(a,b):
    return(a*b//g(a,b))
ans=t[0]
for i in range(n):
    ans=l(ans,t[i])
print(ans)
