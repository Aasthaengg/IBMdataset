N = int(input())
X = list(map(int, input().split()))
 
def calc_power(p):
  P = list(map(lambda x: (x-p)**2, X))
  return sum(P)
 
power = []
_min = min(X)
_max = max(X)

if _min != _max:
  for p in range(_min, _max):
    power.append(calc_power(p))
  print(min(power))
  
else:
  power = calc_power(_min)
  print(power)