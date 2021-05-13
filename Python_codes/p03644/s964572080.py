n=int(input())
ans=0
while 2**ans<=n:
  ans+=1
print(int(2**(ans-1)))