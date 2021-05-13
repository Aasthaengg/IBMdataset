from itertools import accumulate
from collections import deque

N,W=list(map(int,input().split()))
arr=[deque([]) for i in range(4)]

w1,v=list(map(int,input().split()))
arr[0].append(v)

for i in range(N-1):
    w,v=list(map(int,input().split()))
    arr[w-w1].append(v)

for i in range(4):
    arr[i]=sorted(arr[i],reverse=True)
    arr[i]=deque(accumulate(arr[i]))
    arr[i].appendleft(0)

ans=0
for i in range(len(arr[0])):
    for j in range(len(arr[1])):
        for k in range(len(arr[2])):
            for h in range(len(arr[3])):
                weight=(i+j+k+h)*w1+j+2*k+3*h
                value=arr[0][i]+arr[1][j]+arr[2][k]+arr[3][h]
                if weight>W:
                    break
                elif value>ans:
                    ans=value
print(ans)