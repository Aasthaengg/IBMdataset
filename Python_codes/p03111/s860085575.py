# solution

from itertools import product
nim, a, b, c = map(int, input().split())
array = []
for i in range(nim):
  array.append(int(input()))

abc = [0,a,b,c]
ch = [0,1,2,3]
cal = []

for i in product(ch,repeat=nim):
  calc = 0
  su = [0,0,0,0]
  ct = [0,0,0,0]
  temp = list(i)
  for j in range(nim):
    su[temp[j]] += array[j]
    ct[temp[j]] += 1
  if (ct[1]==0)|(ct[2]==0)|(ct[3]==0):
    continue
  for k in range(1,4):
    calc += abs(abc[k]-su[k])
    calc += max((ct[k]-1),0)*10
  cal.append(calc)
    
print(min(cal))