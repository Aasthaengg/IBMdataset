N = int(input())
a = [int(c) for c in input().split()]
c = [0]*8
over = 0
for i in range(N):
    if a[i]>=3200:
        over+=1
    else:
        c[a[i]//400]+=1
 
mi = 8-c.count(0)
ma = mi+over
if mi == 0:
    mi+=1
print(mi,ma)
