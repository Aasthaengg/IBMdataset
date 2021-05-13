import math
X = int(input())

flug=0
while(flug == 0):
  flug2=1
  for i in range(2,round(math.sqrt(X))+1):
    if X%i==0:
      flug2=0
      
  if flug2==1:
    flug=1
    
  else:
    X+=1
    
print(X)