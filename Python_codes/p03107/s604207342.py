S=input()
n0,n1=0,0
for s in S:
  if s=='1':
    n1+=1
  elif s=='0':
    n0+=1
print(min(n1,n0)*2)