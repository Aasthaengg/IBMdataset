from operator import add
from collections import deque
from itertools import accumulate

N,K = map(int,input().split())
S = input()

if N == 1:
  if S == "1" or K >= 1:
    print(1)
  else:
    print(0)
    
else:
  num = []
  cnt = 1
  ans = 0
  M = 2 * K + 1

  for i in range(1,N):
    if S[i] == S[i - 1]:
      cnt += 1
    else:
      num.append(cnt)
      cnt = 1
  num.append(cnt)

  if S[0] == "0":
    num = [0] + num
  
  acc = list(accumulate(num,add))
  acc = [0] + acc
  A = len(acc)
  
  for left in range(0,A,2):
    right = min(A - 1,left + M)
    ans = max((acc[right] - acc[left]),ans)
    
  print(ans)

