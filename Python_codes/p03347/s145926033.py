n=int(input())
a=[int(input()) for _ in range(n)]
if a[0]!=0:
  print(-1)
  exit()
a.reverse()
pre=a[0]
tmp=pre
ans=0
for ai in a[1:]:
  if ai>=pre:
    ans+=tmp
    pre=ai
    tmp=ai
  elif ai+1==pre:
    pre=ai
  else:
    print(-1)
    exit()
ans+=tmp
print(ans)


