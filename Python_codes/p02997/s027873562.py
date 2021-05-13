def output(X):
  for x in X:
    print(*x)

N,K = map(int,input().split())
ALL = N*(N-1)//2
MAX = ALL - (N-1)
if K > MAX:
  print(-1)
  exit()
G = []
req = ALL-K
cnt = 0
for i in range(1,N+1): #1-N
  for j in range(i+1,N+1): #i+1-N
    if i == 1:
      G.append([i,j])
      cnt += 1
    else:
      if cnt >= req:
        print(req)
        output(G)
        exit()
      else:
        G.append([i,j])
        cnt += 1
print(req)
output(G)