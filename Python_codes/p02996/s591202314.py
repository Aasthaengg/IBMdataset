N = int(input())
li = []
for i in range(N):
  l = list(map(int, input().split()))
  li.append(l)
li.sort(key=lambda x: x[1])

cnt = 0
flag = True
for l in li:
  cnt += l[0]
  if cnt > l[1]:
    flag = False
    break
    
if flag:
  print('Yes')
else:
  print('No')