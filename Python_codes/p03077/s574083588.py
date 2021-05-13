import math

N = int(input())
A = [int(input()) for _ in range(5)]

nec = math.ceil(N / min(A))
ans = nec + 4
print(ans)