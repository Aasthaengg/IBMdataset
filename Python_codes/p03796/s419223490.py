n = int(input())
power = 1

for x in range(1, n+1):
  power = (power * x) % (10 ** 9 + 7) 
  
print(power)