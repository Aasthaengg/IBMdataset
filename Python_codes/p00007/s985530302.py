import math

while True:
    try:
        N = int(input())
    except ValueError:
        pass
    else:
        break

lent = 100000
for i in range(N):
    lent *= 1.05
    lent = math.ceil(lent / 1000) * 1000
    
print(lent)