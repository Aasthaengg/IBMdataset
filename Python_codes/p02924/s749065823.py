import sys
readline = sys.stdin.readline

N = int(readline())

# 1 から N - 1までの和になる

def calc(A):
  return ((1 + A) * A) // 2

print(calc(N - 1))