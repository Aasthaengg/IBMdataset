N, A, B , *h = map(int, open(0).read().split())
C = A-B
l = -1
r = 10**12
while l+1<r:
  s = (l+r)//2
  cnt = sum((c-s*B+C-1)//C if c-s*B>0 else 0 for c in h)
  if cnt>s:
    l = s
  else:
    r = s
print(r)