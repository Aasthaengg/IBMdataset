np, cp, tl = map(int, input().split())
bn = [1] + [0 for i in range(np-1)]
ar = []
for i in range(np):
  ar.append(int(input())) 
ar.sort()

lim = ar[0] + tl
num = 1
gto = 1
for i in range(1, np):
  if gto == cp or lim < ar[i]:
    lim = ar[i] + tl
    gto = 1
    num += 1
    bn[i] = num
  else:
    gto += 1
    bn[i] = num

print(bn[-1])