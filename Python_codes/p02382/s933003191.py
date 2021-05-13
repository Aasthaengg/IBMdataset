import math

n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

for p in range(1, 4):
    if p == 1:
        print('{0:f}'.format(sum([abs(a - b) for a, b in zip(x, y)])))
    else:
        print('{0:f}'.format(math.pow(sum([math.pow(abs(a - b), p) for a, b in zip(x, y)]), 1 / p)))

print('{0:f}'.format(max(abs(a - b) for a, b in zip(x, y))))