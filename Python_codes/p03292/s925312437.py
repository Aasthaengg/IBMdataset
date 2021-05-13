a, b, c = map(int, input().split())
x = [a, b, c]
x.sort()
print(x[2] - x[0])