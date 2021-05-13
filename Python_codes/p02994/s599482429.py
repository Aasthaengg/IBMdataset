n,l=map(int,input().split())
ls=range(l,n+l)
if 0 in ls:
    x=0
elif all(i>0 for i in ls):
    x=ls[0]
else:
    x=ls[n-1]
print(int((n*l+(n-1)*n/2-x)))