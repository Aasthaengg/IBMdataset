s=input()

n=len(s)

ans=100000
for i in range(n-2):
  t=str(s[i])+str(s[i+1])+str(s[i+2])
  x=abs(753-int(t))
  
  ans=min(ans,x)
  
print(ans)
