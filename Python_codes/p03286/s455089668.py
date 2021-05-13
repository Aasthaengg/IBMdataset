n = int(input())
m=-2
t=0
pos=0
ans=[]
while n!=t:
  if (n-t)%m == 0:
    ans.insert(0,0)
  else:
    ans.insert(0,1)
  t+=ans[0]*(m//-2)
  m=m*(-2)

if n == 0:
  print(0)
else:
  ans = [str(n) for n in ans]
  print("".join(ans))