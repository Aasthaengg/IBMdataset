li=list(map(int,input().split()))
li.sort()
ans=0
if (li[1]-li[0])%2:
  li[1]+=1
  li[2]+=1
  ans+=1
ans+=li[2]-li[1]
ans+=(li[1]-li[0])//2
print(ans)
