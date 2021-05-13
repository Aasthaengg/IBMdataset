n,k = map(int,input().split())
bitl = [0 for i in range(50)]
al = map(int,input().split())
ansl = [0 for i in range(50)]

for a in al:
  p = 0
  while a:
    bitl[p] += a % 2
    a //= 2
    p += 1
p=0
while k:
  ansl[p] = k % 2
  k //= 2
  p += 1

ans = 0
for i in range(50):
  tmp = 0
  if ansl[i] != 1:
    continue
  else:
    for j in range(i):
      tmp += 2 ** j * max(bitl[j], n-bitl[j])
    tmp +=2 ** i * bitl[i]
    for j in range(i+1, 50):
      if ansl[j] == 0:
        tmp += 2 ** j * bitl[j]
      else:
        tmp += 2 ** j * (n-bitl[j])
  ans = max(ans, tmp)
else:
  tmp = 0
  for j in range(0, 50):
    if ansl[j] == 0:
      tmp += 2 ** j * bitl[j]
    else:
      tmp += 2 ** j * (n - bitl[j])
  ans = max(ans, tmp)

print(ans)

