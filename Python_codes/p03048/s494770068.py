r, b, g, n=map(int, input().split())
rm=n//r
bm=n//b
ans=0
for i in range(rm+1):
  for j in range(bm+1):
    sa=n-r*i-b*j
    if sa<0:
      break
    elif sa%g==0:
      ans+=1
print(ans)