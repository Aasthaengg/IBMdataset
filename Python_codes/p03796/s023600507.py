def training(N) :
  power = 1
  for i in range(1, N + 1) : 
    power = (power * i) % (10 ** 9 + 7)
    
  return power

N = int(input())

print(training(N))