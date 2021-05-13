import math
N = int(input())

for i in reversed(range(N)):
    n = math.sqrt(N)
    if n.is_integer():
        print(int(n ** 2))
        exit()
    N -= 1