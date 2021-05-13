n=input()
k=int(input())
counter=0
nex=0
for i in range(len(n)):
  if n[i]=='1':
    counter+=1
  else:
    nex=n[i]
    break
if nex==0:
  nex='1'
if k>counter:
  print(nex)
else:
  print(1)