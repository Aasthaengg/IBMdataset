import sys

lis = list()

for line in sys.stdin : 
  lis.append(int(line))
  

if (lis[0] - lis[1]) < 0 : 
  print(lis[0] * lis[2])
  
else : 
  sum = lis[1] * lis[2] + (lis[0] - lis[1]) * lis[3]
  print(sum)