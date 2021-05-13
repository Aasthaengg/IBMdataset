n = int(input())
pwr = 1
for i in range(n): 
    pwr *= 1*(i+1)
    pwr = pwr%(10**9+7)
print(pwr)