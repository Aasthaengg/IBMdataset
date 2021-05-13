n=list(input())
lis=[]
for k in range(len(n)):
  lis.append(int(n[len(n)-1-k]))
             
t=0

for k in range(len(lis)):
  if lis[k]==10:
    if k==len(lis)-1:
      t+=1
      break
    else:
      lis[k]=0
      lis[k+1]+=1
  if lis[k]<5:
    t+=lis[k]
  elif lis[k]>5:
    t=t+10-lis[k]
    if k==len(lis)-1:
        t+=1
        break
    else:
        
      lis[k+1]+=1
  elif lis[k]==5:
    if k==len(lis)-1:
      t+=5
    else:
      t+=5
      if lis[k+1]<5:
        pass
      else:
        lis[k+1]+=1
print(t)