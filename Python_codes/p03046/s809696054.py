M,K=map(int,input().split())
if (1<<M)<=K or (K==1 and M==1):
  print(-1)
  exit()
if M==1:
  print('0 0 1 1')
  exit()
X=[]
for i in range(1<<M):
  if i!=K:
    X.append(i)
X.append(K)
for i in range((1<<M)-1,-1,-1):
  if i!=K:
    X.append(i)
X.append(K)
print(*X)