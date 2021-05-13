s=list(input())
t=list(input())

a=len(s)
b=len(t)

ans=[]
ans1=[]

if b>a:
  print('UNRESTORABLE')
  

else:
  for i in range(a-b+1):
    ch=0
    for j in range(b):
      if s[i+j]==t[j] or s[i+j]=='?':
        ch+=1
        
    if ch==b:
      ans.append(i)
      
  if len(ans)==0:
    print('UNRESTORABLE')
    
  else:
    for k in ans:
      r=[]
      for h in range(a):
        if s[h]=='?':
          r.append('a')
        else:
          r.append(s[h])
       
      f=0
      for l in range(k,k+b):
        r[l]=t[f]
        f+=1
        
      ans1.append(r)
    ans2=[]
    for w in ans1:
      u=''.join(w)
      ans2.append(u)
    
    ans2.sort()
    print(ans2[0])