from math import factorial as f
def cmb(n,r):
    if n<r:return 0
    else:return f(n)//f(r)//f(n-r)

n,a,b=map(int,input().split())
v=sorted(map(int,input().split()),reverse=True)
m=sum(v[:a])/a
print(m)
i=j=a-1
while 1:
    if i==0:break
    elif v[i-1]!=v[a-1]:break
    else:i-=1
while 1:
    if j==n-1:break
    elif v[j+1]!=v[a-1]:break
    else:j+=1
ans=0
if i==0:
    for r in range(a,b+1):ans+=cmb(j+1,r)
else:
    ans+=cmb(j-i+1,a-i)
print(ans)