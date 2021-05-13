n=int(input())
d={}
for i in range(1, n+1):
  x=int(input())
  d[i] = x
if d[1] == 2:
  print(1)
  exit()
tmp = d[1]
ans=1
for _ in range(n):
  ans+=1
  tmp = d[tmp]
  #print(tmp)
  if tmp == 2:
    print(ans)
    exit()
print(-1)