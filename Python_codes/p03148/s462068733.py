from heapq import heappush, heappop
N, K, *L = map(int, open(0).read().split())
ls = []
for t,d in zip(*[iter(L)]*2):
  ls += [(d,t)]
used = []
cnt = [0]*(N+1)
hq = []
S = set()
ls.sort(reverse=True)
m = 0
for i in range(K):
  d,t = ls[i]
  cnt[t] += 1
  m += d
  if cnt[t]>1:
    used.append(d)
  S.add(t)
used.sort(reverse=True)
m += len(S)**2
for i in range(K,N):
  d,t = ls[i]
  if t not in S:
    heappush(hq,(-d,t))
ans = [m]
while used:
  d = used.pop()
  while hq:
    if hq[0][1] not in S:
      break
    heappop(hq)
  else:
    break
  m -= d
  n,s = heappop(hq)
  m += -n+2*len(S)+1
  ans.append(m)
  S.add(s)
print(max(ans))