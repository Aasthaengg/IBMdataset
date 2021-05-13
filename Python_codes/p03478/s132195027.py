n,a,b=map(int,input().split())
cnt=0
for i in range(1,n+1):
  ans=0
  i=str(i)
  for j in range(len(i)):
    x=int(i[j])
    ans+=x
  if a<=ans<=b:
    i=int(i)
    cnt+=i
    

print(cnt)
