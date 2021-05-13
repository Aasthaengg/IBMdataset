h,w,d = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for i in range(q)]
spot = [0] * (h*w)
for ki,v in enumerate(a):
  for kj,i in enumerate(v):
    spot[i-1] = (ki,kj)
cumsum = [[0] for i in range(d)]
for start in range(d):
  for j in range(start,h*w-d,d):
    h1,w1 = spot[j]
    h2,w2 = spot[j+d]
    dist = abs(h1-h2) + abs(w1-w2)
    cumsum[start].append(dist+cumsum[start][-1])
for l,r in lr:
  l -= 1
  r -= 1
  mod = l % d
  L,R = l//d,r//d
  ans = cumsum[mod][R]-cumsum[mod][L]
  print(ans)