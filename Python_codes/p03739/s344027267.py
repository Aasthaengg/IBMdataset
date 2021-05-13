import copy

n=int(input())
a=[int(x) for x in input().rstrip().split()]

now=0
ans1=0
for i in range(n):
  now+=a[i]
  if i%2==0:
    if now<=0:
      ans1+=abs(now)+1
      now=1
  else:
    if 0<=now:
      ans1+=abs(now)+1
      now=-1

now=0
ans2=0
for i in range(n):
  now+=a[i]
  if i%2==0:
    if 0<=now:
      ans2+=abs(now)+1
      now=-1
  else:
    if now<=0:
      ans2+=abs(now)+1
      now=1
print(min(ans1,ans2))