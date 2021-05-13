ans=0
a,b=map(int,input().split())
while True:
  if a*2<=b:
    ans+=1
    a=a*2
  else:
    break
print(ans+1)