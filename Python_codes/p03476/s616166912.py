import math
Q = int(input())

li = [0]
cnt = 0
for i in range(3, 10**5+1, 2):
  flag = True
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      flag = False
  if flag:
    for j in range(2, int(math.sqrt((i+1)//2)+1)):
      if ((i+1)//2) % j == 0:
        flag = False
  if flag:
    cnt += 1
  li.append(cnt)
  
for i in range(Q):
  l, r = map(int, input().split())
  if l == 1:
    ans = li[r//2]
  else:
    ans = li[r//2] - li[l//2-1]
  print(ans)
