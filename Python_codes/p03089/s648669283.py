n=int(input())
a=list(map(int,input().split()))
d=[]
while a:
  f=True
  for i in range(len(a)):
    if a[-i-1]==len(a)-i:
      d=[len(a)-i]+d
      a[len(a)-i-1:]=a[len(a)-i:]
      f=False
      break
  if f:
    break
if a:
  print(-1)
else:
  for i in d:
    print(i)