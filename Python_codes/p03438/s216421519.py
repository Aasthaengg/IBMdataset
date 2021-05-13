N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ab = [0] * N
for i in range(N):
    ab[i] = B[i] - A[i]
m = sum(ab)
ab = sorted(ab, reverse=True)
import math
f, g = 0, 0
for c in ab:
    if c > 0:
        f += math.ceil(c/2)
    elif c < 0:
        g += -c
if max(f, g) <= m:
    result = "Yes"
else:
    result = "No"
print(result)