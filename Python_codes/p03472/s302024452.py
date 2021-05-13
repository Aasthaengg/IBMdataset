import math
n,h=map(int,input().split())
m=0
b=[]
for _ in range(n):
    A,B=map(int,input().split())
    if A>m: m=A
    b.append(B)
b.sort()
j=n-1
ans=0
while True:
    if j<0 or b[j]<=m:
        ans+=math.ceil(h/m)
        break
    h-=b[j]
    j-=1
    ans+=1
    if h<=0: break
print(ans)