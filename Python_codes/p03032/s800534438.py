import copy
from collections import deque
N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for k in range(K+1): #0-K
  for left in range(N+1): #0-N
    for right in range(N-left+1):
      push = k - (left + right)
      if push < 0 or push > left+right:
        continue
      Acopy = copy.copy(A)
      Acopy = deque(Acopy)
      B = []
      for t in range(left):
        temp = Acopy.popleft()
        B.append(temp)
      for t in range(right):
        #print(left,right)
        temp = Acopy.pop()
        B.append(temp)
      B.sort()
      wa = sum(B)-sum(B[:push])
      ans = max(ans,wa)
print(ans)
