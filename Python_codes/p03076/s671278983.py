import itertools
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

menu = [a, b, c, d, e]

permutations = list(itertools.permutations(range(5)))

ans = float('inf')
for p in permutations:
    time = 0
    for i in range(5):
        time += menu[p[i]]
        if i != 4:
            time = math.ceil(time / 10) * 10
    ans = min(ans, time)

print(ans)