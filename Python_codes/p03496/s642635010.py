n = int(input())

a = list(map(int,input().split()))

maxabs =(a[0])
maxidx = 0
for i in range(n):
    if abs(a[i]) >abs(maxabs):
        maxabs = a[i]
        maxidx = i 
res = []
for i in range(n):
    if a[i]*maxabs<0:
        a[i] += maxabs
        res.append((maxidx+1,i+1)) 
if maxabs>0:
    for i in range(1,n):
        res.append((i,i+1))
elif maxabs<0:
    for i in range(n,1,-1):
        res.append((i,i-1))

print(len(res))
for x,y in res:
    print(x,y)
