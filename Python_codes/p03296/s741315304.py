n=int(input())
l=list(map(int,input().split()))
s=[]
i=0
c=1
while True:
  if i==n-1:
    s.append(c)
    break
  if l[i]!=l[i+1]:
    s.append(c)
    c=0
  c+=1
  i+=1
ans=0
for i in s:
  ans+=i//2
print(ans)