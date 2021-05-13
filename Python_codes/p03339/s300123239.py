n=int(input())
s=str(input())
s=list(s)
tempw=s.count("W")
ans=n-tempw
cnt=n-tempw
if s[0]=="E":
  ans=ans-1
  cnt=cnt-1
for i in range(1,n):
  if s[i-1]=="W":
    cnt=cnt+1
  if s[i]=="E":
    cnt=cnt-1
  ans=min(ans,cnt)  
print(ans)