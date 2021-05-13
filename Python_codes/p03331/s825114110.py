def getter(i):
  res=0
  while True:
    res+=i%10
    i//=10
    if i==0:
      break
  return res
n=int(input())
digit=0
hoge=n
while True:
  hoge//=10
  if hoge==0:
  	break
  digit+=1
a=10**digit
if n-a>0:
  res=1+getter(n-a)
  print(res)
  exit()
else:
  print("10")

