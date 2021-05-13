n = int(input())
a = list(map(int, input().split()))
L = [0 for _ in range(n)]
L[0] = a[0]
for i in range(1, n):
  L[i] = L[i-1] + a[i]
delay = 0
all_over = 0
anti_delay = 0
anti_all_over = 0
if a[0] != 0:
  antiL = L[:]
  sign = (a[0] > 0) - (a[0] < 0)
  for i in range(1, n):
    L[i] += delay
    if L[i] <= 0 and sign == -1:
      delay += 1 - L[i]
      all_over += 1 - L[i]
      L[i] = 1
    elif L[i] >= 0 and sign == 1:
      delay -= L[i] + 1
      all_over += L[i] + 1
      L[i] = -1
    sign *= -1
  if antiL[0] < 0:
    sign = 1
    anti_delay = 1 - antiL[0]
    anti_all_over = 1 - antiL[0]
  else:
    sign = -1
    anti_delay = -(antiL[0] + 1)
    anti_all_over = antiL[0] + 1
  for i in range(1, n):
    antiL[i] += anti_delay
    if antiL[i] <= 0 and sign == -1:
      anti_delay += 1 - antiL[i]
      anti_all_over += 1 - antiL[i]
      antiL[i] = 1
    elif antiL[i] >= 0 and sign == 1:
      anti_delay -= antiL[i] + 1
      anti_all_over += antiL[i] + 1
      antiL[i] = -1
    sign *= -1
  print(min(anti_all_over, all_over))
else:
  posL = L[:]
  negL = L[:]
  pos_delay, neg_delay = 1, -1
  pos_all_over, neg_all_over = 1, 1
  sign = 1
  for i in range(1, n):
    posL[i] += pos_delay
    if posL[i] <= 0 and sign == -1:
      pos_delay += 1 - posL[i]
      pos_all_over += 1 - posL[i]
      posL[i] = 1
    elif posL[i] >= 0 and sign == 1:
      pos_delay -= posL[i] + 1
      pos_all_over += posL[i] + 1
      posL[i] = -1
    sign *= -1
  sign = -1
  for i in range(1, n):
    negL[i] += neg_delay
    if negL[i] <= 0 and sign == -1:
      neg_delay += 1 - negL[i]
      neg_all_over += 1 - negL[i]
      negL[i] = 1
    elif negL[i] >= 0 and sign == 1:
      neg_delay -= negL[i] + 1
      neg_all_over += negL[i] + 1
      negL[i] = -1
    sign *= -1
  print(min(pos_all_over, neg_all_over))
