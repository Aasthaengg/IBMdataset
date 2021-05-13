import bisect

a, b = map(int, input().split())

towers = []
last = 0
for i in range(1, 1000):
    towers.append(last+i)
    last += i

diff = b - a

print(towers[diff-1] - b)