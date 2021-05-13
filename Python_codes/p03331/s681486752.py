n=int(input())
while n%10==0 and n!=10:
  n=n//10
if n==10:
  print(10)
else:
  s=str(n)
  ans=0
  for i in range(len(s)):
    ans+=int(s[i])
  print(ans)