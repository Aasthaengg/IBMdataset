from collections import deque
n=int(input())
A=sorted(list(map(int,input().split())))
A=deque(A)

N=[]
left,right=A.popleft(),A.pop()
for i in A:
    if i<0:
        N.append([right,i])
        right -=i
    else:
        N.append([left,i])
        left -=i
N.append([right,left])
print(right-left)
for i in N:print(*i)