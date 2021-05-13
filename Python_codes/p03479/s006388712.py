x,y=[int(x) for x in input().rstrip().split()]
ans=1
now=x
for i in range(x,y-1):
  if now*2<=y:
    now=now*2
    ans+=1
  else:
    break
print(ans)


