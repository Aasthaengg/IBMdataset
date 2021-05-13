N, M = map(int,input().split())
KA = [list(map(int,input().split())) for i in range(N)]

dic = {}

for i in range(N):
  for j in range(len(KA[i])-1):
    if KA[i][1+j] not in dic.keys():
      dic[KA[i][1+j]] = 1
    else:
      dic[KA[i][1+j]] += 1
      
ans = 0

for i in dic:
  if dic[i] == N:
    ans += 1
    
print(ans)