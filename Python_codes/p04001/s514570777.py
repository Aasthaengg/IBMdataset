s=list(input())
n=len(s)
ans=0
for i in range(2**(n-1)):
  ball=s[0]
  for j in range(n-1):
    if (i>>j)&1:
      ball+="+"+s[j+1]
    else:
      ball+=s[j+1]
  ans+=eval(ball)
print(ans)