s=list(input())

l=[]
cnt=0

for i in s:
  if i=='A' or i=='C' or i=='G' or i=='T':
    cnt+=1
  else:
    if cnt!=0:
      l.append(cnt)
      cnt=0

l.append(cnt)
print(max(l))