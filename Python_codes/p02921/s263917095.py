a=list(input())
b=list(input())
r=0
for ii in range(len(a)):
  if a[ii]==b[ii]:
    r+=1
print(r)