N,K=map(int,input().split())

if K > N :
  print(0)
elif K == N:
  print(1)
else:
  print(N - K + 1)