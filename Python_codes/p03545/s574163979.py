s=input()
ans=[]

for i in range(2**3):
  a=int(s[0])
  for j in range(3):
    if ((i>>j)&1):
      a+=int(s[j+1])
    else:
      a-=int(s[j+1])
      
  if a==7:
    ans.append(i)
    
u=ans[0]
ans1=[]
for j in range(3):
  if ((u>>j)&1):
      ans1.append('+')
  else:
      ans1.append('-')
      
print(s[0]+ans1[0]+s[1]+ans1[1]+s[2]+ans1[2]+s[3]+'=7')