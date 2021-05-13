n=int(input())
a=26
b=1
import math
import string
array=list(string.ascii_lowercase)
while n>a:
  b+=1
  a+=26**b
if b==1:
  print(array[n-1])
else:
  c=b-1
  d=n-a
  brray=[0]
  crray=[d]
  for i in range(c):
    brray.append(math.ceil(crray[i]/(26**(c-i))))
    crray.append(crray[i]%(26**(c-i)))
  ans=array[brray[1]-1]
  if c>1:
    for j in range(2,b):
      ans=ans+array[brray[j]-1]
  ans=ans+array[crray[c]-1]
  print(ans)