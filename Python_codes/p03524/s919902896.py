s=str(input())

lis=[0]*3

lis[0]=s.count("a")
lis[1]=s.count("b")
lis[2]=s.count("c")

n=len(s)//3

ans="YES"

for i in lis:
  if n<=i<=n+1:
    continue
  else:
    ans="NO"
    
print(ans)