N, A, B = map(int, input().split())
h = []
for i in range(N):
  h += [int(input())]

Th = 2*max(h)//B
Tl = 0
while Tl+1<Th:
  t = (Th+Tl)//2
  d = []
  for i in range(N):
    c = h[i]
    d += [c-B*t]
  for i in range(N):
    c = d[i]
    if c<=0:
      continue
    t -= c//(A-B) if c%(A-B)==0 else c//(A-B)+1
    if t<0:
      Tl = (Th+Tl)//2
      break
  else:
    Th = (Th+Tl)//2
print(Th)