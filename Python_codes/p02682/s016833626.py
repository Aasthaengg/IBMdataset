x,y,z,k=map(int,input().split())
s=min(k,x)
k=k-s
if(k>0):
    k=k-min(k,y)
if(k>0):
    f=min(k,z)
    s=s-f
print(s)