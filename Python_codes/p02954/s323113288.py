s=input()
n=len(s)
flag=1
j=0
a=[]
for i in range(1,n):
  if flag and s[i]=='L':flag=0
  elif not flag and s[i]=='R':
    a+=[s[j:i]]
    j=i
    flag=1
a+=[s[j:n]]
fans=[]
for i in a:
  cr=i.count('R')
  cl=i.count('L')
  ans=[0]*(cr+cl)
  if cr<cl:
    if cl%2:
      ans[cr-1]=(cr+cl)//2
      ans[cr]=(cr+cl+1)//2
    else:
      ans[cr-1]=(cr+cl+1)//2
      ans[cr]=(cr+cl)//2
  else:
    if cr%2:
      ans[cr-1]=(cr+cl+1)//2
      ans[cr]=(cr+cl)//2
    else:
      ans[cr-1]=(cr+cl)//2
      ans[cr]=(cr+cl+1)//2
  fans+=ans
print(*fans)