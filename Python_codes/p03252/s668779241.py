s1,s2=input(),input()
d1,d2={},{}
for i,j in zip(s1,s2):
  if i not in d1:
    d1[i]=1
  else:
    d1[i]+=1
  if j not in d2:
    d2[j]=1
  else:
    d2[j]+=1
d1=sorted(d1.items(),key=lambda x:x[1])
d2=sorted(d2.items(),key=lambda x:x[1])
for i,j in zip(d1,d2):
  if i[1]!=j[1]:
    print('No')
    break
else:
  print('Yes')