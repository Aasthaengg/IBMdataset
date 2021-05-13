import math

def main(a, b):
    return math.ceil((a + b) / 2)

a,b = map(int, input().split())
print(main(a, b))