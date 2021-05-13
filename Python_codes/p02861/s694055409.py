import itertools
import math

N = int(input())
L = []
for i in range(N):
    X, Y = map(int, input().split())
    L.append((X, Y))

total = 0
cnt = 0
for l in itertools.permutations(L):
    cnt += 1
    for i in range(1, N):
        total += math.sqrt((l[i][0]-l[i-1][0])**2 + (l[i][1]-l[i-1][1])**2)

print(total/cnt)