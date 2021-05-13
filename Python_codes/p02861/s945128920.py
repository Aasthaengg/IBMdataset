from itertools import permutations
from math import factorial

N = int(input())
town = {}
route = permutations(range(0,N))

for i in range(N):
    town[i] = tuple(map(int,input().split()))

Sum = 0

for v in route:
    for i in range(N-1):
        Sum += ((town[v[i+1]][0] - town[v[i]][0])**2 + (town[v[i+1]][1] - town[v[i]][1])**2)**(0.5)

ans = Sum/factorial(N)

print(ans)