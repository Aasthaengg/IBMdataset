from math import gcd
a,b,c,d,e,f=map(int,input().split())
g=gcd(a,b)
a=a//g
b=b//g
G=gcd(c,d)
c=c//G
d=d//G
axby=[0]*1000
czdw=[0]*1000
for x in range(100):
    for y in range(100):
        if a*x+b*y<(a-1)*(b-1):
            axby[a*x+b*y]=1
for z in range(100):
    for w in range(100):
        if c*z+d*w<(c-1)*(d-1):
            czdw[c*z+d*w]=1
A=[]
C=[]
for i in range(1000):
    if axby[i]==1:
        A.append(i)
for i in range(1000):
    if czdw[i]==1:
        C.append(i)
i=(a-1)*(b-1)
while i<=(f//(100*g))+5:
    A.append(i)
    i+=1
j=(c-1)*(d-1)
while j<=(f//G)+5:
    C.append(j)
    j+=1
n=len(A)
m=len(C)
dis=0
ans=[0,0]
for i in range(n):
    for j in range(m):
        if 100*g*A[i]+G*C[j]<=f and G*C[j]<=e*g*A[i] and not(A[i]==C[j]==0):
            if dis<=(100*G*C[j])/(100*g*A[i]+G*C[j]):
                dis=(100*G*C[j])/(100*g*A[i]+G*C[j])
                ans[0],ans[1]=A[i],C[j]
print(100*g*ans[0]+G*ans[1],G*ans[1])


