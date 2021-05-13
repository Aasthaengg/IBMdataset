from collections import deque

N=int(input())
b=list(map(int,input().split()))

op=[0]*N

for i in range(N-1,-1,-1):
    for j in range(len(b)-1,-1,-1):
        if b[j]==j+1:
            op[i]=j+1
            break
    
    if op[i]==0:
        print(-1)
        exit(0)

    b=[b[i] for i in range(op[i]-1)]+[b[i] for i in range(op[i],len(b))]

for op1 in op:
    print(op1)
