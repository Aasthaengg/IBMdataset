N,W = map(int,input().split())
total1 = 0
total2 = 0
if N>1:
  total1 = N*(N-1)//2
else:
  total1 = 0

if W>=2:
  total2 = W*(W-1)//2
else:
  total2 = 0
print(total1+total2)