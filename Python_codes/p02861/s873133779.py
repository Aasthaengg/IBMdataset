from itertools import permutations

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append(complex(x, y))

s = 0
c = 0
for perm in permutations(range(N), N):
    c += 1
    for i in range(N-1):
        s += abs(points[perm[i]] - points[perm[i+1]])

print(s / c)