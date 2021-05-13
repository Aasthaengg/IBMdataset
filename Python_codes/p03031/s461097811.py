N,M = map(int,input().split())
K = [0 for m in range(M)]
count = 0

for m in range(M):
  K[m] = list(map(int,input().split()))
P = list(map(int,input().split()))

for i in range(2**N):
  op = [0]*N
  for j in range(N):
    if ((i>>j) & 1):
      op[N-1-j] = 1
      
  flag = True
  
  for k in range(M):
    S = 0
    for l in range(K[k][0]):
      S += op[K[k][l+1]-1]
    if S % 2 != P[k]:
      flag = False
  if flag:
    count += 1
    
print(count)