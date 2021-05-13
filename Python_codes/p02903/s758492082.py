h, w, a, b = map(int, input().split())

ans = [['0' for _ in range(w)] for _ in range(h)]
for i in range(b):
    for j in range(a):
        ans[i][j] = '1'

for i in range(b, h):
    for j in range(a, w):
        ans[i][j] = '1'

for x in ans:
    print(''.join(x))
