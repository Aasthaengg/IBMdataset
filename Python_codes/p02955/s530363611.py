import math

N, K = map(int, input().split(" "))
As = list(map(int, input().split(" ")))

S = sum(As)
l = []
i = 1
ans = 1

while i*i <= S:
  if S % i == 0:
    l.append(i)
    l.append(S//i)
  i += 1

l.sort(reverse=True)

for i in l:
  ext = 0
  exts = []
  for j in As:
    exts.append(j % i)
    ext += (j % i)
  if ext % i != 0:
    continue
  else:
    p = 0
    exts.sort()
    cnt = ext//i
    for k in range(0, N - cnt):
      p += exts[k]
    if p <= K:
      ans = i
      break

print(ans)