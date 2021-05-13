import math
X = int(input())
n = (int(math.sqrt(X)))**2
for b in range(2, int(math.sqrt(X))+2):
    for p in range(1, 10):
        if (b**p > n) and (b**p <= X):
            n = b**p
print(n)
