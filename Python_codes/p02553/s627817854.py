a, b, c, d = map(int, input().split())

print(max([x * y for x in [a, b] for y in [c, d]]))