s=list(input())


c=[]
for i in range(3):
  cnt=0
  if s[i]=='R':
    
    
    while i<3:
      if s[i]=='R':
        cnt+=1
        i+=1
        
      else:
        break
        
  c.append(cnt)
    
print(max(c))