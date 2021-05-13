n=int(input())
a=[0]+list(map(int,input().split()))
b=list(map(int,input().split()))+[0]
c=[[0,0]for i in range(n)]
p=0
mod=10**9+7
d=1
for i in range(n,0,-1):
    if a[i-1]!=a[i]:
        c[i-1]=[1,a[i]]
    else:
        c[i-1]=[0,a[i]]
for i in range(n):
    if b[i]!=b[i+1]:
        if c[i][0]==1:
            if b[i]!=c[i][1]:
                print(0)
                break
        else:
            if b[i]<=c[i][1]:
                c[i]=[1,b[i]]
            else:
                print(0)
                break
    else:
        if c[i][0]!=1:
            c[i]=[0,min(b[i],c[i][1])]
        else:
            if c[i][1]>b[i]:
                print(0)
                break
    if c[i][0]!=1:
        d=d*c[i][1]%mod
else:
    print(d)