import math
N = int(input())
mx = 0
for i in range(math.ceil(math.sqrt(N))+1):
    if i**2 <= N and i**2 >= mx:
        mx = i**2
        
print(mx)