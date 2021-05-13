N,M = map(int, input().split())
P = [list(map(int, input().split())) for m in range(M)]
C = (N+1)*[0]
D = {}

for p,y in sorted(P,key=lambda x: x[1]):
  C[p]+= 1
  D[y]="%06d%06d" % (p,C[p])

for p,y in P:
  print(D[y])