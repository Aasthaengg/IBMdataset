import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, read().split())
h, w = 100, 100
print(h, w)
ans = [['#'] * w for _ in range(h // 2)] + [['.'] * w for _ in range(h // 2)]
if a > 1:
    cnt = 0
    flag = False
    for i in range(0, h, 2):
        for j in range(0, w, 2):
            ans[i][j] = '.'
            cnt += 1
            if a - 1 == cnt:
                flag = True
                break
        if flag:
            break
if b > 1:
    cnt = 0
    flag = False
    for i in range(h // 2 + 1, h, 2):
        for j in range(0, w, 2):
            ans[i][j] = '#'
            cnt += 1
            if b - 1 == cnt:
                flag = True
                break
        if flag:
            break
for aa in ans:
    print(''.join(aa))
