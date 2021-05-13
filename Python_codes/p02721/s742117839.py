N, K, C = map(int, input().split())
S = input()

L = []
R = []
holiday = 0

for i in range(N):
  if holiday:
    holiday -= 1
  elif S[i] == 'o':
    L.append(i)
    holiday = C
holiday = 0
for i in range(N-1, -1, -1):
  if holiday:
    holiday -= 1
  elif S[i] == 'o':
    R.append(i)
    holiday = C
R = R[::-1]
out = set(L) and set(R)
if len(L) == K:
  for l, r in zip(L, R):
    if l == r: print(l+1)