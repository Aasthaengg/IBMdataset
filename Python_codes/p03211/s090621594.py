s=input()
n=len(s)

ans=753
for i in range(n-2):
  t=int(s[i]+s[i+1]+s[i+2])
  ans=min(ans, abs(753-t))
print(ans)