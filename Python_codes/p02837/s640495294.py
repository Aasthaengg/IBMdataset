n = int(input())
tst = [[] for i in range(n)]
for i in range(n):
  a = int(input())
  for j in range(a):
    x,y = map(int,input().split())
    tst[i].append([x,y])
ans = 0
for bit in range(1<<n):
  liars = [0]*n
  check = 1
  for i in range(n):
    if (bit>>i)&1:
      liars[-1-i] = 1
  for i in range(n):
    if liars[i]:
      for l in tst[i]:
        if l[1]!=liars[l[0]-1]:
          check = 0
          break
  temp = 0
  if check:
    temp = sum(liars)
  ans = max(ans,temp)
print(ans)