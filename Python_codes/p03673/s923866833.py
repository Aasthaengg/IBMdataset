from collections import deque
N = int(input())
A = list(map(int,input().split()))

Q = deque([])
for i in range(N):
  if i%2 ==0 :
    Q.append(A[i])
  else:
    Q.appendleft(A[i])
#print(Q)
if N%2 == 0:
  print(*Q)
else:
  Q.reverse()
  print(*Q)