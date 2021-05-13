n, m = map(int, input().split())
S = set()
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    S.add((a, b))

for i in range(1, n-1):
    if (0, i) in S and (i, n-1) in S:
        print('POSSIBLE')
        exit()
else:
    print('IMPOSSIBLE')
