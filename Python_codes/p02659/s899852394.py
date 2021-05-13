a,b=input().split()
A=int(a)
bb=b.replace(".","")
B=int(bb)
#print(B)
c=A*B
C=str(c)
if C[:-2]=='':
  print(0)
else:
  print(C[:-2])