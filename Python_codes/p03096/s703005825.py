import bisect
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
app = [0 for i in range(200001)]
mod = 10**9+7
pair = []
for i in range(n):
  x = a[i]
  if app[x] != 0 and i != app[x]:
    pair.append([app[x],i+1])
  app[x] = i+1
pair.sort()
ps = len(pair)
cntls = []
order = []
sumtot = []
for i in range(ps-1,-1,-1):
  [s,t] = pair[i]
  if i == ps-1:
    cntls.append([-s,1])
    order.append(-s)
    sumtot.append([-s,1])
  elif t>-cntls[0][0]:
    cntls.append([-s,1])
    order.append(-s)
    sumtot.append([-s,sumtot[-1][1]+1])
  else:
    x = bisect.bisect_right(order,-t)
    cntls.append([-s,sumtot[x-1][1]+1])
    order.append(-s)
    sumtot.append([-s,(sumtot[-1][1]+sumtot[x-1][1]+1)%mod])
if pair == []:
  print(1)
else:
  print((sumtot[-1][1]+1)%mod)