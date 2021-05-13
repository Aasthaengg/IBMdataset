n=int(input())
v=list(map(int,input().split()))
v.sort()
ans=(v[0]+v[1])/2
cnt=2
while cnt<len(v):
  ans=(ans+v[cnt])/2
  cnt+=1
  
print(ans)