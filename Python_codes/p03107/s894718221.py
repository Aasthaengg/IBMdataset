S=input()
n0,n1=0,0
for s in S:
  if s=='0':
    n0+=1
  else:
    n1+=1
print(min(n0,n1)*2)