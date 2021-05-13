N=int(input())
X=0
for i in range(1,1000):
  X+=i
  if X==N:
    P=[[] for j in range(i+1)]
    X=0
    for j in range(i):
      for k in range(i-j):
        P[j].append(k+X+1)
      for k in range(i-j):
        P[k+j+1].append(k+X+1)
      X+=i-j
    print('Yes')
    print(i+1)
    for j in range(i+1):
      print(len(P[j]),end=' ')
      print(*P[j])
    exit()
print('No')