import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

x = min(A, B, C, D, E)
ans = math.ceil(N / x) + 4
print(ans)