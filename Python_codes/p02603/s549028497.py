from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()+[0]

money=1000
ans=1000
kabu=0

for i in range(n):
  if a[i]<a[i+1]:
    t_kabu=money//a[i]
    kabu+=t_kabu
    money-=t_kabu*a[i]
  elif a[i]>a[i+1]:
    money+=kabu*a[i]
    kabu=0

  ans=max(ans,money)

print(ans)