N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
m = min(A, B, C, D, E)
import math
n = math.ceil(N/m)
ans = n + 4
print(ans)