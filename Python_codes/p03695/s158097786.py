n=int(input())
a=list(map(int,input().split()))
c=[0]*9

for r in a:
  x=r//400
  if x>8:
    x=8
  c[x]+=1
ans=0
for i in range(9):
  if i==8:
    if ans==0:
      mn=1
      mx=n
    else:
      mn=ans
      mx=ans+c[i]
  if c[i]!=0:
    ans+=1

print("{} {}".format(mn,mx))