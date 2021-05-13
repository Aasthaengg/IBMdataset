def nextLunlun(l):
  l[-1]+=1
  for i in range(len(l)-1):
    if abs(l[-i-1]-l[-i-2])>=2 or l[-i-1]==10:
      l[-i-2]+=1
      l[-i-1]=0

  if l[0]>=10:
    l.insert(0,1)
    l[1]=0
    
  for i in range(len(l)-1):
    if abs(l[i]-l[i+1])>=2:
      l[i+1]=max(0,l[i]-1)
  
  return l

l=[0]
n=int(input())

for i in range(n):
  nextLunlun(l)
for num in l:
  print(num,end='')
print()