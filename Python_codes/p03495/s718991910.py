n,k=map(int,input().split())
a=list(map(int,input().split()))
n=[0]*200000
x=[]
for i in a:
    n[i-1]+=1
for i in n:
    if i!=0:
        x+=[i]
y=len(x)
z=y-k
if z<=0:
    print(0)
else:
    x.sort()
    print(sum(x[:z]))