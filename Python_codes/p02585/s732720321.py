from collections import deque
import sys, copy,itertools
input = sys.stdin.readline

n, k = map(int,input().split())
#P = list(map(int,input().split()))
P = list(map(lambda x : int(x) - 1, input().split())) #ひとつづつずらす
C = list(map(int,input().split()))
SCORE = [0]*(n+1)

max_score = -10**12
for i in range(n):
  x = i
  TEMPMAX = [-10**9] * (n+1)
  for j in range(1, n+1):
    SCORE[j] = SCORE[j-1] + C[P[x]]
    TEMPMAX[j]= max(TEMPMAX[j-1], SCORE[j])
    x = P[x]
    if x == i:
      break
  if j >= k:
    max_score = max(max_score,TEMPMAX[k])
  elif SCORE[j] < 0:
    max_score = max(max_score, TEMPMAX[j])
  else:
    m = k//j
    a = SCORE[j] *(m-1) + TEMPMAX[j]
    b = SCORE[j] *m + TEMPMAX[k % j]
    max_score = max(max_score, a, b)
print(max_score)