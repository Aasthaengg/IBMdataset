n,m,c=list(map(int,input().split()))

b=list(map(int,input().split()))
a=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)
#print(a[0][1])
total=0
for v in a:
    combined1=[x*y for (x,y) in zip(b,v)]
    if sum(combined1)+c > 0:
        total+=1
print(total)
