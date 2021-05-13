import sys
import math
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(float, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

a, b = inm()
a = int(a)
b = int(b * 100 + 0.1)
print(a*b // 100)