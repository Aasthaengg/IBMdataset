import math
n = int(input())
xs = [int(_) for _ in input().split()]
ys = [int(_) for _ in input().split()]

print(sum([abs(x-y) for x, y in zip(xs, ys)]))
print(math.sqrt(sum([pow(abs(x-y),2) for x, y in zip(xs, ys)])))
print(math.pow(sum([pow(abs(x-y),3) for x, y in zip(xs, ys)]), 1/3))
print(max([abs(x-y) for x, y in zip(xs, ys)]))