N, P=map(int, input().split())
A=list(map(int, input().split()))
odd=[]
even=[]
for a in A:
  if a%2==0:
    even.append(a)
  else:
    odd.append(a)
amod=len(odd)
amev=len(even)
evonly=2**amev

from math import factorial
if P==0:
  evod=0
  i=0
  while amod>=i:
    evod+=factorial(amod)//(factorial(i)*factorial(amod-i))
    i+=2
  print(evonly*evod)
else:
  evod=0
  i=1
  while amod>=i:
    evod+=factorial(amod)//(factorial(i)*factorial(amod-i))
    i+=2
  print(evonly*evod)