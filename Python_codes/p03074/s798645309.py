from collections import deque
N, K = map(int, input().split())
S = deque(input())
T = []
P = []
pre = S[0]
cnt = 0
while S:
  s = S.popleft()
  cnt += 1
  if pre != s:
    cnt -= 1
    T += [cnt]
    P += [pre]
    pre = s
    cnt = 1
T += [cnt]
P += [pre]

cum_T = T[:]
for i in range(len(T)-1):
  cum_T[i+1] = cum_T[i] + T[i+1]

cum_T += [0]
l = len(P)
ans = 0
for i in range(l):
  if P[i] == '1':
    r = min(l-1, i+2*K)
    ans = max(ans,-cum_T[i-1]+cum_T[r] )
  else:
    r = min(l-1, i+2*K-1)
    ans = max(ans, -cum_T[i-1]+cum_T[r])
print(ans)