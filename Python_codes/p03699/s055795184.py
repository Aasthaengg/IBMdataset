n=int(input())
s=[int(input()) for i in range(n)]
t=sum(s)
if t%10!=0:
  print(t)
else:
  s.sort()
  a=1
  for i in range(n):
    if s[i]%10!=0:
      print(t-s[i])
      a=0
      break
  if a:
    print(0)