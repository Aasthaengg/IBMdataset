X=list(input())
ans=0
cnt=0
for i in range(len(X)):
  if cnt==0:
    if X[i]=="T":
      ans+=1
    else:
      cnt+=1
  else:
    if X[i]=="T":
      cnt-=1
    else:
      cnt+=1
    
print(ans+cnt)