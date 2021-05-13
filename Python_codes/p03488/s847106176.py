import sys
s=input()
n=len(s)
x,y=map(int,input().split())
lst=list(s.split("T"))
if len(lst)==1:
    if x==len(s) and y==0:
        print("Yes")
    else:
        print("No")
    sys.exit()
v=[0]*(2*n+1)
u=[0]*(2*n+1)
a=len(lst[0])
b=len(lst[1])
v[n+a]=1
u[n+b]=1
u[n-b]=1
for i in range(2,len(lst)):
    l=len(lst[i])
    if i%2==0:
        h=[0]*(2*n+1)
        for i in range(2*n+1):
            if i-l>=0:
                if v[i-l]==1:
                    h[i]=1
            if i+l<=2*n:
                if v[i+l]==1:
                    h[i]=1
        v=h
    else:
        h=[0]*(2*n+1)
        for i in range(2*n+1):
            if i-l>=0:
                if u[i-l]==1:
                    h[i]=1
            if i+l<=2*n:
                if u[i+l]==1:
                    h[i]=1
        u=h
if v[n+x]==1 and u[n+y]==1:
    print("Yes")
else:
    print("No")