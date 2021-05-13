N, K = map(int, input().split())
border = []
inx = 0
while K > 1:
  border.append(K)
  K = (K + 1) >> 1
  inx += 1
border.append(1)
border.reverse()
pre = 1
cnt = []
for i in range(1, len(border)):
  if N < border[i]:
    cnt.append(N - pre + 1)
    break
  elif N == border[i]:
    cnt.append(border[i] - pre)
    cnt.append(1)
    break
  else:
    cnt.append(border[i] - pre)
    pre = border[i]
if N >= border[-1]:
  cnt.append(N - border[-1] + 1)
ans = 0
for c in cnt:
  ans += c * 0.5 ** inx
  inx -= 1
print(ans/N)