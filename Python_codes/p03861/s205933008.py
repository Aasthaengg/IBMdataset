a,b,x=map(int,input().split())
k=a//x
l=a%x
p=b//x
q=b%x
if l==0:
    print(p-k+1)
else:
    print(p-k)
