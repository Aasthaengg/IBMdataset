l=list(map(int, input().split()))
l.sort()
base=l[2]-l[1]
if (l[1]-l[0])%2==1:
  base+=1
  l[1]+=1
ans=base+(l[1]-l[0])//2
print(ans)
