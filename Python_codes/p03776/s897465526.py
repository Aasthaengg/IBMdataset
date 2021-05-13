n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
print(sum(v[:a])/a)
 
import math
def cmb(n,r):
    f = math.factorial
    return int(f(n) // f(r) // f(n-r))
x,y=v.count(v[a-1]),v[:a].count(v[a-1])
if v[0]==v[a-1]:
   ans=sum(cmb(x,i) for i in range(a,min(b,x)+1))
else:
    ans=cmb(x,y)
print(ans)    