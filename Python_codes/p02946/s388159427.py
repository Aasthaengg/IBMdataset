N = input().split()
K = int(N[0])
X = int(N[1])
for i in range(X-K+1,X+K):
  print(i,end=' ')