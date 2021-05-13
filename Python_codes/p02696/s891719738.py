import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())
def f(x: int) -> int: return ((a * x) // b) - (a * (x // b))
print(f(min(b-1, n)))