N,M = map(int,input().split())
K = []
sum = 0
if N==1:
  W=list(map(int,input().split()))
  W.pop(0)
  K+=W
  print(len(K))
  exit()
for i in range(N):
  W=list(map(int,input().split()))
  W.pop(0)
  K+=W
for T in range(1,len(K)+1):
  B=K.count(T)
  if B == N:
    sum+=1
print(sum)
