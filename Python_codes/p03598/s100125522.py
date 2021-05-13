N = int(input())
K = int(input())
X = list(map(lambda a: int(a), input().split(" ")))

print(2 * sum([min([x, abs(K - x)]) for x in X]))