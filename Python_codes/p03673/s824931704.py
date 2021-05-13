from collections import deque

N = int(input())
A = list(map(int,input().split()))

ANS = deque()
for i in range(N):
  if i % 2 == 0:
    ANS.append(A[i])
  else:
    ANS.appendleft(A[i])
    
ANS = list(ANS)
if N % 2 == 1:
  ANS = ANS[::-1]
  
print(" ".join(map(str,ANS)))
