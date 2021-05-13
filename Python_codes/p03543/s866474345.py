n=str(input())
a=0
for i in range(1,len(n)):
  if n[i]==n[i-1]:
    a+=1
  else:
    a=0
  if a>=2:
    print('Yes')
    break
if a<2:
  print('No')
