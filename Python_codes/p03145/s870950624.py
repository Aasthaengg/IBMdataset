import math

def solve_A():
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    area = s * (s-a) * (s-b) * (s-c)
    return math.sqrt(area)

print(int(solve_A()))