a=input()
ans=len(a)*(len(a)-1)//2+1
b={}
for i in a:
  if i in b:
    b[i]+=1
  else:
    b[i]=1
for i in b:
  ans-=b[i]*(b[i]-1)//2
print(ans)