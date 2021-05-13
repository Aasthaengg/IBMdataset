N,M = map(int, input().split())
if N==1 and M==1:
  result = 0
if 0<=N and N<=1 and 2<=M:
  result = M*(M-1)//2
if 2<=N and 0<=M and M<=1:
  result = N*(N-1)//2
if 2<=N and 2<=M:
  result = (N*(N-1)+M*(M-1))//2
  
print(result)