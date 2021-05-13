N,M = map(int,input().split())
LIKE = [True] * M

for i in range(N):
  KA = list(map(int,input().split()))
  A = KA[1:]
  
  for i in range(M):
    if not (i+1) in A:
      LIKE[i] = False
      
print(LIKE.count(True))