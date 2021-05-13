import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

min_v = min(A, B, C, D, E)
print((N - 1) // min_v + 1 + 4)