N,K,S=map(int, input().split())
L=[S]*K
for _ in range(N-K):
  if S==10**9:
    L.append(1)
  else:
    L.append(S+1)

for x in L:
  x=str(x)
  print(x,end=' ')