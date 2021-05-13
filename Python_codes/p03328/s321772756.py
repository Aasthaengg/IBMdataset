ab = list(map(lambda x: int(x), input().split(" ")))
a = ab[0]
b = ab[1]

n = b - a - 1

x = n * (n + 1) // 2 - a

print(x)
