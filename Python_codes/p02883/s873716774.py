n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))[::-1]
l,r=10**12+1,-1
while l-r>1:
    t=(l+r)//2
    s=k
    for i,j in zip(a,b):
        if t<i*j:s-=i-t//j
    if s<0:r=t
    else:l=t
print(l)