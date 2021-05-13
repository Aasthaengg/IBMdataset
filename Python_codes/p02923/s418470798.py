m=int(input())
h=list(map(int,input().split()))
ans1=[]
ans=0
if m>1:
  
  for x in range(m-1):
    if h[x]<h[x+1]:
      ans1.append(ans)
      ans=0
    else:
      ans+=1
      ans1.append(ans)
    
  
    
  print(max(ans1))

else:
  print(0)
