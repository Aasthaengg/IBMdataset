n,t=map(int,input().split())
ts= list(input().split())
ts = [int(i) for i in ts]

ans=0
flag=False
for i in range(0,len(ts)):
  #print(ts[i],flag)
  if flag:
    if ts[i]-ts[i-1] <= t:
      ans+=ts[i]-ts[i-1]
    else:  
      ans+=t
  else:
    if ts[i]<=t and i!=len(ts)-1:
      ans=ts[i+1]
    else:
      if ts[i]-ts[i-1] <= t:
        ans=ts[i]
        
      else:  
        ans=ts[i-1]+t
        flag=True
  #print("ans",ans)

print(ans+t)