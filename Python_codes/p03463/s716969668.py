import sys

n, a, b = map(int, input().split())

print("Alice") if (max(a, b) - (min(a,b) + 1)) % 2 != 0 else print("Borys")