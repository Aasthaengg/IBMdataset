from sys import stdin
def input():
    return stdin.readline().strip()

h, w = map(int, input().split())
s = [input() for _ in range(h)]

def check(x, y, up, down, left, right):
    if s[x][y] == '.':
        return 0
    if up and s[x-1][y] == '#':
        return 0
    if down and s[x+1][y] == '#':
        return 0
    if left and s[x][y-1] == '#':
        return 0
    if right and s[x][y+1] == '#':
        return 0
    else:
        print('No')
        exit()

# (0, y)
check(0, 0, False, True, False, True)
for y in range(1, w-1):
    check(0, y, False, True, True, True)
check(0, w-1, False, True, True, False)

# (x, y)
for x in range(1, h-1):
    check(x, 0, True, True, False, True)
    for y in range(1, w-1):
        check(x, y, True, True, True, True)
    check(x, w-1, True, True, True, False)

# (h-1, y)
check(h-1, 0, True, False, False, True)
for y in range(1, w-1):
    check(h-1, y, True, False, True, True)
check(h-1, w-1, True, False, True, False)

print('Yes')