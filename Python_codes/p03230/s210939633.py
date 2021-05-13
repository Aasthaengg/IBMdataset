n=int(input())
qi=0
for i in range(1000):
    if i*(i+1) ==n*2:
        qi=i
if qi==0 : 
    print("No")
    exit()
print("Yes")
print(qi+1)
from itertools import combinations as com
A=[[] for i in range(qi+1)]
now=1
for i,j in com([i for i in range(qi+1)],2):
    A[i].append(now) ; A[j].append(now)
    now+=1

for i in range(qi+1):
    print(qi, *A[i])