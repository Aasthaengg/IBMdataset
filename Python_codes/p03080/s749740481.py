N=int(input())
S=list(input())
Chk=0
for i in S:
  if i=='R':
    Chk+=1
  else:
    Chk-=1
ans='Yes' if Chk>0 else 'No'
print(ans)