n,k=map(int,input().split())
r,s,p=map(int,input().split())
a=list(input())
ans1=[]

ans=0
for i in range(n):
  x=a[i]
  if i-k>=0:
    if x==a[i-k]:
      if ans1[i-k]==0:
        if x=='r':
          ans1.append(p)
        elif x=='p':
          ans1.append(s)
        else:
          ans1.append(r)
          
      else:
        ans1.append(0)
    else:
      if x=='r':
          ans1.append(p)
      elif x=='p':
          ans1.append(s)
      else:
          ans1.append(r)
  else:
    if x=='r':
          ans1.append(p)
     
    elif x=='p':
          ans1.append(s)
        
    else:
          ans1.append(r)

print(sum(ans1))