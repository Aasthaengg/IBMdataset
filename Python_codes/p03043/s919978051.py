N,K = map(int,input().split())
P = 0
for i in range(1,N+1):
  j = 0
  t = 1
  while t>0:
    t = K-i*2**j
    j = j+1
  P = P+(1/N)*(1/2)**(j-1)
print(P)