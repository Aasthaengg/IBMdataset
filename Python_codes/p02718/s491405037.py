a,b=map(int,input().split())
c=list(map(int,input().split()))
d=sum(c)
e=(4*b)
f=0
for i in c:
    if(i*e>=d):
        f+=1

if(f>=b):
    print('Yes')
else:
    print('No')

