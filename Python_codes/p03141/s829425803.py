from collections import deque
N=int(input())

C=[]
D=0
for _ in range(N):
    a,b=map(int,input().split())
    C.append((a,b))
    D+=b
    
C.sort(key=lambda x:x[0]+x[1])
C=deque(C)

i=0
A=0
while C:
    (a,b)=C.pop()
    if i==0:
        A+=a+b
    i^=1
print(A-D)
