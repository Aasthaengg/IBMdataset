N,*a = map(int,open(0).read().split())
a.sort()
flag = True
for i in range(1,N):
  if a[i]==a[i-1]:
    print('NO')
    flag=False
    break
if flag ==True:
  print('YES')