N, M = map(int, input().split())
routes = [[] for i in range(N-1)]
ans = [0]*(N-1)
li = []
for i in range(M):
  r = list(map(int, input().split()))
  if r[0] == 1:
    li.append(r[1])
    ans[r[1]-2] = 1
  elif r[1] == 1:
    li.append(r[0])
    ans[r[0]-2] = 1
  else:
    routes[r[0]-2].append(r[1])
    routes[r[1]-2].append(r[0])
    
flag = True
while 0 in ans:
  tmp = []
  if li == []:
    flag = False
    break
  for num in li:
    for route in routes[num-2]:
      if ans[route-2] == 0:
        ans[route-2] = num
        tmp.append(route)
  li = tmp
  
if flag:
  print('Yes')
  for i in range(N-1):
    print(ans[i])
else:
  print('No')