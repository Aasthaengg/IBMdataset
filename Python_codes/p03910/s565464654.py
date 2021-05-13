n=int(input())
l=[]
ans=0
for i in range(1,n+1):
  l.append(i)
  ans+=i
  if n<=ans:
    break
if n<ans:
  l.remove(ans-n)
  print(*l)
else:
  print(*l)