n,*a=map(int,input().split())
l=[int(input()) for i in range(n)]
ans=float("inf")
for i in range(4**n):
  table=[0 for g in range(3) ]
  temp=i
  pre=0

  for j in range(n):

    if temp%4==3:temp//=4;continue
    if table[temp%4]:
      table[temp%4]+=l[j]
      pre+=10
    else:table[temp%4]=l[j]
    temp//=4
  if 0 in table:continue
  for g in range(3):
    pre+=abs(a[g]-table[g])
  ans=min(ans,pre)
print(ans)