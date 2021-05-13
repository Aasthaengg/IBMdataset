N = int(input())
K = int(input())
X = list(map(int, input().split()))

print(sum(min(2 * x, 2 * (K - x)) for x in X))
