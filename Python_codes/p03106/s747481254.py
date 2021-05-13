a,b,k=map(int,input().split())
cnt=0
for i in reversed(range(1,101)):
  if a%i==0 and b%i==0:
    cnt+=1
  if cnt==k:
    print(i)
    break