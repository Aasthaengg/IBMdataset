N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
import math
x = math.ceil(N / (min(A, B, C, D, E)))
ans = 5 + (x - 1)
print(ans)
