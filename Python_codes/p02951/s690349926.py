a, b, c = list(map(int, input().split()))
r = c - (a - b)
print(r if r > 0 else 0)