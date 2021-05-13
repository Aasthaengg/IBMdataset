n=int(input())
l=sorted(list(map(int,input().split())))
ans,s=1,0
for u in l:
  if 2*s>=u:ans+=1
  else:ans=1
  s+=u
print(ans)
