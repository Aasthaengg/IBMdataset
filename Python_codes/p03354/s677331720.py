N, M = map(int, input().split())
P = list(map(int, input().split()))

root = [i for i in range(N + 1)]
comp_size = [1] * (N + 1)

def root_find(x):
  y = root[x]
  if x == y:
    return x
  else:
    z = root_find(y)
    root[x] = z
    return z

def merge(x, y):
  rx = root_find(x)
  ry = root_find(y)
  sx = comp_size[rx]
  sy = comp_size[ry]
  if sx >= sy:
    comp_size[rx] += comp_size[ry]
    root[ry] = root[rx]
  else:
    comp_size[ry] += comp_size[rx]
    root[rx] = root[ry]

for _ in range(M):
  a, b = map(int, input().split())
  merge(a, b)
#print(root)

answer = 0
for i in range(N):
  if root_find(P[i]) == root_find(i + 1):
    answer += 1
#print(root)
print(answer)