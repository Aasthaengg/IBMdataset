import itertools
import math
N = int(input())
P = [0] * N 
for i in range(N):
    P[i] = list(map(int,input().split()))
distance = 0
for root in itertools.permutations(P,N):
    start = root[0]
    for r in root:
        distance += pow((r[0]-start[0])**2 + (r[1]-start[1])**2,1/2)
        start = r
print(distance/math.factorial(N))
