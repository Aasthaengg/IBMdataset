import math
n = int(input())
x, y = [list(map(int, input().split())) for _ in range(2)]
for p in (1,2,3,0):
    if p == 0:
        print(max(abs(x-y) for x, y in zip(x,y)))
    else:
        print(math.pow(sum(abs(x-y) ** p for x, y in zip(x,y)), 1.0 / p))