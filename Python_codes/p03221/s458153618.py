N, M = map(int, input().split())

dic = {i:[(0,0)] for i in range(1,N+1)}
lst = ['']*M

for i in range(M):
  p,y = map(int, input().split())
  dic[p].append((y,i))
  
for k in dic:
  dic[k].sort(key=lambda x:x[0])
  for i in range(1,len(dic[k])):
    lst[dic[k][i][1]] = str(k).zfill(6)+str(i).zfill(6)
    
for l in lst:
  print(l)