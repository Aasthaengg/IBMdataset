import math
L = [int(input()) for _ in range(5)]
L.sort(key=lambda x: (x-1)%10)
print(L[0]+sum(map(lambda x:math.ceil(x/10)*10, L[1:])))