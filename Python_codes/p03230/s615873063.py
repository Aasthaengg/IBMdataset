import sys
N = int(input())

K = 1
while K * (K-1) // 2 < N:
  K += 1

if K * (K-1) // 2 != N:
  print("No")
  sys.exit(0)

vs = [ [] for _ in range(K) ]
k = 0
for i in range(K):
  for j in range(K):
    if i <= j: continue
    vs[i].append(k)
    vs[j].append(k)
    k += 1

print('Yes')
print(K)
for v in vs:
  print(len(v), end="")
  print(" ", end="")
  print(" ".join([str(x+1) for x in v]))
