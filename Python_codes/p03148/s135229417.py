from collections import Counter
n,k = map(int,input().split())
td = [list(map(int,input().split())) for i in range(n)]
td.sort(key = lambda x:x[1],reverse=True)
ans = list(range(k))
ansv = sum((td[i][1] for i in range(k)))
c = Counter((td[i][0] for i in range(k)))
cnt = len(c)
ansv += len(c)**2
ptr = k
ansls = [ansv]
for i in range(k-1,-1,-1):
  t,d = td[ans[i]]
  if ptr < n and c[t] > 1:
    while ptr < n and c[td[ptr][0]] >= 1:
      ptr += 1
    if ptr >= n:
      break
    ansv = ansv-d+2*cnt+1+td[ptr][1]
    c[t] -= 1
    c[td[ptr][0]] += 1
    cnt += 1
    ptr += 1
    ansls.append(ansv)
print(max(ansls))