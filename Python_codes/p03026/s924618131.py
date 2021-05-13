N = int(input())
E = [set() for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  E[a].add(b)
  E[b].add(a)
cs = list(map(int, input().split()))
cs.sort()
M = sum(cs[:-1])
ds = [-1]*N
ds[0] = cs.pop()
q = [0]
while q:
  c = q.pop()
  ns = E[c]
  for n in ns:
    if ds[n] < 0:
      ds[n] = cs.pop()
      q.append(n)
print(M)
print(" ".join(map(str, ds)))
