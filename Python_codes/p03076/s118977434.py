from math import ceil
a=[int(input()) for i in range(5)]
ans=10
sum=0
for i in a:
  x=(i-1)%10+1
  ans=min(ans,x)
  sum+=ceil(i/10)*10
if ans==10:
  print(sum)
else:
  print(sum+ans-10)