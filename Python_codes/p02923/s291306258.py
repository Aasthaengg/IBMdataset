n=int(input())
h=list(map(int,input().split()))
cnt=0
ans=0
kaisu=0
while cnt<len(h)-1:
  if h[cnt]< h[cnt+1]:
    
    ans=max(ans,kaisu)
    #print(ans)
    kaisu=0
    cnt+=1
  else:
    cnt+=1
    kaisu+=1

ans=max(ans,kaisu)
    
print(ans)