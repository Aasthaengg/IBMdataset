l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
bef=l[0]
for i in l:
  ans+=abs(bef-i)
  bef=i
print(ans)
