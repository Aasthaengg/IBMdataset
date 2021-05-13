l=input()

ans=0
num=0

for i in l:
  if i=="A" or i=="G" or i=="C" or i=="T":
    num+=1
  else:
    ans=max(num,ans)
    num=0
ans=max(ans,num)
    
print(ans)
    
