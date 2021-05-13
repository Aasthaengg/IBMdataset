# AtCoder
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
sc = sorted(c.items(), key=lambda x: x[0], reverse=True)
sides = []
for side, nums in sc:
    if nums >= 4:
        sides.append(side)
        sides.append(side)
    elif nums >= 2:
        sides.append(side)
if 1 >= len(sides):
    print(0)
    exit()

s = sorted(sides, reverse=True)
ans = s[0]*s[1]
print(ans)
