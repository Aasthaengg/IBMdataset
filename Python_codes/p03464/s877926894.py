n=int(input())
a=list(map(int,input().split()))
if a[-1]!=2:exit(print(-1))
l=r=2
for i in a[::-1]:
  if (l-1)//i==r//i:exit(print(-1))
  l=(0--l//i)*i
  r=(r//i)*i+i-1
print(l,r)