N,K = map(int,input().split())
ret = K
for i in range(2,N+1):
  ret *= K-1
print(ret)