n=int(input())
a=list(map(int,input().split()))
ans=1
odd=1
for i in a:
  ans*=3
  if(i%2==0):
    odd*=2
print(ans-odd)