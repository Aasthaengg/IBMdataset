_ = input()
P = [int(i) for i in input().split()]

vmin = max(P)
vmax = 0

cnt = 0
for p in P:
  if p <= vmin:
    cnt += 1
  if p < vmin:
    vmin = p
  if vmax < p:
    vmax = p
    
print(cnt)