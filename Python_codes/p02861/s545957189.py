import itertools
import math

N = int(input())
town = [list(map(int,input().split())) for _ in range(N)]

S = 0
for P in itertools.permutations(range(N)):
    for i in range(N-1):
        s, t = P[i+1], P[i]
        S += math.sqrt((town[s][0]-town[t][0]) ** 2 + (town[s][1]-town[t][1]) ** 2)

for i in range(1,N+1):
    S /= i

print(S)