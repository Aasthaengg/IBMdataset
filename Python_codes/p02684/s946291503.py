n,k=map(int,input().split())
a=list(map(int,input().split()))
t=[0 for i in range(n+1)]
town=1
for i in range(n+1):
    t[town]+=1
    if t[town]==2:
        break
    town=a[town-1]
r=0
sy=0
town=1
while t[town]!=2:
    r+=1
    town=a[town-1]
for i in range(n):
    sy+=1
    town=a[town-1]
    if t[town]==2:
        break
town=1
if r>=k:
    for i in range(k):
        town=a[town-1]
    print(town)
else:
    for i in range(r):
        town=a[town-1]
    k=k-r
    m=k//sy
    k=k-m*sy
    for k in range(k):
        town=a[town-1]
    print(town)
        
    

