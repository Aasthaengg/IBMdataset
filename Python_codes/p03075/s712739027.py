from itertools import combinations

positions = [int(input()) for _ in range(5)]
k = int(input())

distances = [abs(p1 - p2) for p1, p2 in combinations(positions, 2)]
result = all([d <= k for d in distances])

if result:
    print('Yay!')
else:
    print(':(')
