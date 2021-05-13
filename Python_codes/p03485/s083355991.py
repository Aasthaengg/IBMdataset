import math
try:
    a, b = map(int, input().split())
    mean = (a+b)/2
    print(math.ceil(mean))
except EOFError:
    pass