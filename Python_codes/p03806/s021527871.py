from itertools import groupby, accumulate, product, permutations, combinations
def solve():
  ans = float('inf')
  N, A, B = map(int, input().split())
  mae = [list(map(int, input().split())) for _ in range((N+1)//2)]
  usiro = [list(map(int, input().split())) for _ in range(N-(N+1)//2)]
  if N==1:
    a,b,c = mae[0]
    if a*B==b*A:
      return c
    return -1
  mae_lis = [[float('inf')]*201 for _ in range(201)]
  mae_lis[0][0] = 0
  for p in product([0,1],repeat=(N+1)//2):
    a,b,c = 0,0,0
    for i in range((N+1)//2):
      if p[i]==1:
        a += mae[i][0];b += mae[i][1];c += mae[i][2]
    mae_lis[a][b] = min(mae_lis[a][b],c)
  usiro_lis = [[float('inf')]*201 for _ in range(201)]
  usiro_lis[0][0] = 0
  for p in product([0,1],repeat=N-(N+1)//2):
    a,b,c = 0,0,0
    for i in range(N-(N+1)//2):
      if p[i]==1:
        a += usiro[i][0];b += usiro[i][1];c += usiro[i][2]
    usiro_lis[a][b] = min(usiro_lis[a][b],c)
  for i in range(1,201):
    for j in range(1,201):
      c = mae_lis[i][j]
      if c==float('inf'):
        continue
      for k in range(201):
        if (i+k)*B%A!=0:
          continue
        l = (i+k)*B//A - j
        if l<0 or l>200 or usiro_lis[k][l]==float('inf'):
          continue
        ans = min(ans,c+usiro_lis[k][l])
  for k in range(1,201):
    if k*B%A!=0:
      continue
    l = k*B//A
    if l>200 or usiro_lis[k][l]==float('inf'):
      continue
    ans = min(ans,usiro_lis[k][l])
  return ans if ans<float('inf') else -1
print(solve())