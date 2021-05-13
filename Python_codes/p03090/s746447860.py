import sys
import math

# get input
input = sys.stdin.readline()

N = int(input)

# number of connections
M = (N*(N-1)/2)-N/2
print(math.ceil(M))

# NG sum
X = N + 1 - N % 2
for i in range(1, N+1):
    for j in range(i+1,N+1):
        if not i + j == X:
            print(i, " ", j)

