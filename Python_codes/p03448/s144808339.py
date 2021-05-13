import math
A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for i in range(A +1):
    Y = X -i*500
    
    for j in range(B + 1):
        Z = Y - j*100
        if Z >= 0 and Z/50 <= C:
            count += 1

print(str(count))