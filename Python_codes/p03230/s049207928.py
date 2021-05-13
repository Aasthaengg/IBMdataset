#17:27
n = int(input())
k = int((2*n)**.5)
if k*(k+1)//2 != n:
  print('No')
  exit()
ans = [[x for x in range(k)]]
now = k
for j in range(k):
  tmp = []
  for i in range(j+1):
    tmp.append(ans[i][j])
  for i in range(j+1,k):
    tmp.append(now)
    now += 1
  ans.append(tmp)
print('Yes')
print(k+1)
for x in ans:
  print(k,' '.join(list(map(lambda y:str(y+1),x))))