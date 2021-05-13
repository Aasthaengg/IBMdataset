n,m=map(int,input().split())
dic = {}
for i in range(1,n+1):
  dic[i]=0
for i in range(m):
  a,b = map(int,input().split())
  dic[a] += 1
  dic[b] += 1
ret = 'YES'
for i in range(1,n+1):
  if dic[i]%2==1:
    ret = 'NO'
    break
print(ret)