from itertools import permutations
from math import sqrt
n = int(input())
positions = [tuple(map(int, input().split())) for _ in range(n)]


def calc_distance(i, j):
    return sqrt(pow((positions[i][0] - positions[j][0]), 2) + pow((positions[i][1] - positions[j][1]), 2))


ans = 0
count = 0
for tmp in permutations(range(n)):
    for i in range(len(tmp) - 1):
        ans += calc_distance(tmp[i], tmp[i + 1])
    count += 1

print(ans / count)
