a, b, c = map(int, input().split())
print(min(a*b, a*c, b*c) if all(i%2 for i in [a, b, c]) else 0)