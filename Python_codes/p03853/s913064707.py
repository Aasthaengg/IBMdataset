H,W=map(int, input().split())

C = [input() for i in range(H)]
D = []
for i in range(H):
  D.append(C[i])
  D.append(C[i])

for i in range(H*2):
  print(D[i])