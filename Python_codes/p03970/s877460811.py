a=list(input())
b=list('CODEFESTIVAL2016')
s=0
for i,j in zip(a,b):
  s+=1 if i!=j else 0
print(s)