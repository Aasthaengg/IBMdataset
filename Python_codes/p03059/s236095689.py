import itertools
import math
a, b, t = map(int, input().split())
sum = 0
for i in range(1,21):
    if a * i <= t:
        sum += b
print(sum)