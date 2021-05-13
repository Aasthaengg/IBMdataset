import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
m = min(A, B, C, D, E)
print(math.ceil(N / m) + 4)
