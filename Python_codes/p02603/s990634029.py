n=int(input())
a=list(map(int,input().split()))
mone=1000
kabu=0
for i in range(n-1):
  if a[i]<=a[i+1]:
    kabu+=mone//a[i]
    mone%=a[i]
  else:
    mone+=kabu*a[i]
    kabu=0
mone+=kabu*a[-1]
print(mone)