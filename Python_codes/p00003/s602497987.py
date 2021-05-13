import itertools
import operator

line = int(input())
inputs = [input() for _ in range(line)]

def is_right_triangle(a, b, c):
    a, b, c = list(sorted([a,b,c]))
    return a**2 + b**2 == c**2

for line in inputs:
    a, b, c = line.split()
    print("YES" if is_right_triangle(int(a), int(b), int(c)) else "NO")