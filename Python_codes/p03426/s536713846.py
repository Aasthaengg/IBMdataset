H, W, D = map(int, input().split())
M = H * W
A = [list(map(int, input().split())) for i in range(H)]

a_to_ij = {}
for i, aa in enumerate(A):
  for j, a in enumerate(aa):
    a_to_ij[a] = (i, j)

cost = {}
def calc_cost(s):
  global cost
  t = s
  pre_i, pre_j = a_to_ij[s]
  c = cost[(s, s)] = 0
  while t + D <= M:
    t += D
    i, j = a_to_ij[t]
    c += abs(i-pre_i) + abs(j-pre_j)
    cost[(s, t)] = c
    pre_i, pre_j = i, j

for n in range(1, D+1):
  calc_cost(n)

ans = []
Q = int(input())
for i in range(Q):
  L, R = map(int, input().split())
  s = L % D
  if s == 0:
    s = D
  ans.append(cost[(s, R)] - cost[(s, L)])

print(*ans, sep='\n')