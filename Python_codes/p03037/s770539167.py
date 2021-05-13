n, m = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(m)]

L = []
R = []
L_append = L.append
R_append = R.append
for l, r in LR:
    L.append(l)
    R.append(r)

min_R = min(R)
max_L = max(L)
if min_R >= max_L:
  ans = min_R +1 - max_L
else:
  ans = 0
  
print(ans)