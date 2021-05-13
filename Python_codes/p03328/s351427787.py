a, b = list(map(lambda x : int(x), input().split(" ")))
print(int((b - a) * (b - a - 1) / 2) - a)