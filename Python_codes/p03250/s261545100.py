a, b, c = list(map(int, input().split()))

print(10 * max([a, b, c]) + sum([a, b, c]) - max([a, b, c]))
