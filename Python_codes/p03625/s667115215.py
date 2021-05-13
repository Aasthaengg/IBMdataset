# solution
import io
import math

data=int(input())

array=list(map(int, input().split()))
array.sort()
tmp=[]
i=data-1
while i>0:
  if array[i]==array[i-1]:
    tmp.append(array[i])
    i-=2
  else:
    i-=1
if len(tmp)>=2:
  print(tmp[0]*tmp[1])
else:
  print(0)