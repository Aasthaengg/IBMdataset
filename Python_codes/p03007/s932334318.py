from collections import deque
N = int(input())
A = sorted(list(map(int,input().split())))
A = deque(A)
C = []
while len(A)>1 and A[-1]<=0:
    a = A.pop()
    b = A.pop()
    C.append((a,b))
    A.append(a-b)
if len(A)==1:
    x = A[0]
else:
    B = deque(list(A)[:-1])
    while B[-1]>0:
        a = B.popleft()
        b = B.pop()
        C.append((a,b))
        B.appendleft(a-b)
    B.append(A[-1])
    while len(B)>1:
        a = B.pop()
        b = B.popleft()
        C.append((a,b))
        B.append(a-b)
    x = B[0]
print(x)
for i in range(N-1):
    print(C[i][0],C[i][1])