N, C, K = list(map(int, input().split()))
T = []
for i in range(N):
  T.append(int(input()))

bus = []
departure=0

T.sort()

for passenger in T:
  if bus == []:
    bus.append(passenger)
    
  elif passenger <= bus[0]+K and len(bus)<=(C-1):
    bus.append(passenger)
  
  else:
    bus.clear()
    departure+=1
    bus.append(passenger)
    
if bus != []:
  print(departure + 1)
else:
  print(departure)