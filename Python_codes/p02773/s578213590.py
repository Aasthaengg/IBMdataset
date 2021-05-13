N = int(input())
D = {}

for n in range(N):
  S = input()
  D[S] = D.get(S,0)+1

L = max(D.values())

for k,v in sorted(D.items()):
  if v==L:
    print(k)