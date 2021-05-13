a,b=map(int,input().split())
ans=0
if max(a,b)==a:
  ans=ans+a
  a=a-1
  if max(a,b)==a:
    ans=ans+a
    a=a-1
  elif max(a,b)==b:
    ans=ans+b
    b=b-1
elif max(a,b)==b:
  ans=ans+b
  b=b-1
  if max(a,b)==a:
    ans=ans+a
    a=a-1    
  elif max(a,b)==b:
    ans=ans+b
    b=b-1      
print(ans)   
    
