n=int(input())
s=[int(input()) for _ in range(n)]
t=sum(s)
if t%10!=0 or t==0:
  print(t)
else:
  ans=0
  s.sort()
  for i in s:
    if i%10!=0:
      ans=t-i
      break
  print(ans)
