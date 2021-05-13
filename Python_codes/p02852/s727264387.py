import sys
n,m=map(int,input().split())
s=input()
ans=[]
current=n
while current>0:
  for i in range(m):
    if current-(m-i)<0:
      continue
    if s[current-(m-i)]=='0':
      current-=(m-i)
      ans.append(str(m-i))
      break
    if i==m-1:
      print(-1)
      sys.exit()
ans.reverse()
print(' '.join(ans))