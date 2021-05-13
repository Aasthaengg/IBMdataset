X = int(input())

# solve
c = 100
y = 0

import math

while c < X:
    # overflow?
    # c = c + math.floor(c * 0.01)
    # c += math.floor(c/100)
    c += c//100
    y += 1

print(y)