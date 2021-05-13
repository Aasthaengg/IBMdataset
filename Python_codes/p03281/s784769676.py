N=int(input())
 
ans=0
odd=[]
for i in range(1,N+1):
  if i%2!=0:
    odd.append(i)
    
if N  <104:
  pass
else:
  for i in range(105,N+1):
    if i%2!=0:
      tmp=0
      for j in odd:
        if i%j==0:
          tmp+=1
      if tmp==8:
        ans+=1 
print(ans)