L=list()
N=int(input())
for i in range(N):
  n=int(input())
  if n not in L:
    L.append(n)
print(len(L))