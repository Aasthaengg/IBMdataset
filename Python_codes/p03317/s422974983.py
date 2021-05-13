N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(100000):
  if N<=K+i*(K-1) :
    print(i+1)
    exit()