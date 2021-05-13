import math
N = int(input())
A = [int(input()) for _ in range(5)]
a = min(A)
cnt = math.ceil(N/a)
print(5+cnt-1)