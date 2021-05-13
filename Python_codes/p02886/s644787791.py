import itertools

N = int(input())
d = list(map(int, input().split()))

print(sum([i * j for i, j in list(itertools.combinations(d, 2))]))