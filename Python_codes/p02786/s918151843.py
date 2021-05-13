import math
H = int(input())
cnt=0
next=H
while next!=1:
  next= math.floor(next/2)
  cnt +=1
result = sum([2**i for i in range(cnt+1)])
print(result)