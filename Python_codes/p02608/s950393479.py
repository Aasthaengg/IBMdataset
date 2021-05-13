from math import sqrt, floor

N = int(input())
d = [0] * (N+1)

k = floor(sqrt(N))
for x in range(1, k):
    for y in range(1, k):
        for z in range(1, k):
            c = x*x + y*y + z*z + x*y + y*z + z*x
            if 1 <= c <= N:
                d[c] += 1


for i in range(1, N+1):
    print(d[i])
