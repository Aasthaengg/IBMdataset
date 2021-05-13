N,M = map(int,input().split())
cntAB = {i:0 for i in range(1,N+1)}
for _ in range(M):
  a,b = map(int,input().split())
  cntAB[a] += 1
  cntAB[b] += 1
for key, num in cntAB.items():
  if num%2 == 1:
    print('NO')
    exit()
print('YES')