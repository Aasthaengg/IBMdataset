n = int(input())
ns = []
for ni in range(n):
  ns.append(len(ns)+1)
fb = []
for nf in ns:
  if nf % 3 != 0 and nf % 5 != 0:
    fb.append(int(nf))
print(sum(fb))