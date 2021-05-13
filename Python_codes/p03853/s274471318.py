H, W = list(map(lambda x: int(x), input().split(" ")))
C = []
D = []
for i in range(H):
  C.append(input())

for i in range(len(C)):
  D.append(C[i])
  D.append(C[i])

print("\n".join(D))