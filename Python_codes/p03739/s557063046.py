n=int(input())
a=list(map(int,input().split()))
fg=[1,-1]
ret=[0]*2
tot=[0]*2
for i in range(n):
  for j in range(2):
    tot[j]+=a[i]
    if tot[j]*fg[j]<=0:
      ret[j]+=abs(fg[j]-tot[j])
      tot[j]+=fg[j]-tot[j]
    fg[j]*=-1
print(min(ret))