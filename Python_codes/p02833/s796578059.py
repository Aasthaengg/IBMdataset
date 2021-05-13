n=int(input())
if n%2==1:
  ans=0
else:
  m=n//10
  ans=m
  for i in range(1,30):
    ans += m//(5**i)
print(ans)