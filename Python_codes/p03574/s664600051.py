from sys import stdin
def input():
    return stdin.readline().strip()

h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

ans = s.copy()
for i in range(h):
    ans[i] = list(ans[i])

for x in range(h):
    for y in range(w):
        if s[x][y] == '.':
            num = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < h and 0 <= y + dy < w and s[x+dx][y+dy] == '#':
                        num += 1
            ans[x][y] = str(num)

for i in ans:
    print(''.join(i))