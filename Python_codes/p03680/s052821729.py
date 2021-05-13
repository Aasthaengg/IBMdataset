N=int(input())

A=[0]*(N+1)
for k in range(1,N+1):
    A[k]=int(input())

T=[False]*(N+1)
x=1
I=0
while not T[x] and x!=2:
    T[x]=True
    I+=1
    x=A[x]
    
if x==2:
    print(I)
else:
    print(-1)
