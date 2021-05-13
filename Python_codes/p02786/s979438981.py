import math
h=int(input())

cnt=0
for i in range(1,100):
  if h==1:
    break
  h=math.floor(h/2)
  cnt+=2**i

print(cnt+1)