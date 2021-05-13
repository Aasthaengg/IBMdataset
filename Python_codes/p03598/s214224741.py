N = int(input())
K = int(input())
X = tuple(map(int, input().split(' ')))

cost = sum([min(x, K - x) for x in X]) * 2

print(cost)
