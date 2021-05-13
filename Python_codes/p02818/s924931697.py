a,b,k=map(int,input().split())
mod=b-(k-a)
if mod<0:
    a,b=0,0
elif mod<b:
    a,b=0,mod
else:
    a=mod-b
print("{} {}".format(a,b))