s=int(input())
a=[s]

cnt=0
for i in range(10**6):
  if s%2==0:
    s=s/2
    cnt+=1
    if s in a:
      break
    a.append(s)
    
  else:
    s=3*s+1
    cnt+=1 
    if s in a:
      break    
    a.append(s)

print(cnt+1)