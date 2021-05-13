n=int(input())

ans=0
if n<3:
  print(0)
  exit()
while True:
  ans+=1
  if n-3>=3:
    n=n-3
  else:
    break
print(ans)