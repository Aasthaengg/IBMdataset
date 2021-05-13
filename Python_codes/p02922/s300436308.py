A, B = map(int, input().split())
import math
c = math.ceil((B - A) / (A - 1))
print(c + 1)