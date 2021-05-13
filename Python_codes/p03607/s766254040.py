import bisect
n=int(input())
a=[]
lis=[]
for i in range(n):
  inp=int(input())
  a.insert(bisect.bisect_left(a,inp),inp)
ans=0
bef=a[0]
co=0
for i in a[1:]:
  if i!=bef:
    ans+=(co+1)%2
    co=0
    bef=i
  else:
    co+=1
ans+=(co+1)%2
print(ans)