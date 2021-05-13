n=int(input())
if n==1:
    print(1)
    exit()
    
x=[0]*n
y=[0]*n

for i in range(n):
    x[i],y[i]=map(int,input().split())
dis=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        dis.append((x[j]-x[i],y[j]-y[i]))
        
from collections import Counter
c=Counter(dis).most_common()[0]
print(n-c[1])
