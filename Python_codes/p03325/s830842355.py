N=int(input())
a=list(map(int,input().split()))
ans=0
for i in a:
  while 1:
    if i%2!=0:
      break
    i=i//2
    ans+=1
print(ans)