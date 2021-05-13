import math
a = [int(input()) for _ in range(6)]
print(math.ceil(a[0] / min(a[1:])) + 4)