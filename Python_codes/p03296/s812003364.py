n=int(input())
a=list(map(int,input().split()))
ans=0
past=-1
c=1
for i in a:
  if i==past:
    c+=1
    continue
  ans+=c//2
  c,past=1,i
ans+=c//2
print(ans)