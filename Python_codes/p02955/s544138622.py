N, K  = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
dl = []
k = 1
while k ** 2 <= s:
  if s % k == 0:
    dl.append(k)
    dl.append(s // k)
  k += 1
  
cand = []
for d in dl:
  op = 0
  b = [n % d for n in a]
  b.sort()
  b.reverse()
  summod = sum(b)
  for i in range(summod // d):
    op += d - b[i]
  if op <= K:
    cand.append(d)
    
print(max(cand))