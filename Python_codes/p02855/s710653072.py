import sys

readline = sys.stdin.readline
h, w, k = map(int, readline().split())
s = [readline().rstrip() for _ in range(h)]
ans = [[0] * w for _ in range(h)]
peace = 1
not_strawberry = []
for i in range(h):
    strawberry = 0
    for j in range(w):
        if s[i][j] == '#':
            if strawberry == 1:
                peace += 1
                strawberry = 1
            else:
                strawberry = 1
        ans[i][j] = str(peace)
    if not strawberry:
        not_strawberry.append(i)
    else:
        for j in not_strawberry:
            ans[j] = ans[i]
        not_strawberry = []
        peace += 1
if not_strawberry:
    i = min(not_strawberry) - 1
    for j in not_strawberry:
        ans[j] = ans[i]

print('\n'.join(' '.join(i) for i in ans))
