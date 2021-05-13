N, M = map(int, input().split())
teiki_1 = []
teiki_N = []
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        teiki_1.append(a if a != 1 else b)
    if a == N or b == N:
        teiki_N.append(a if a != N else b)
if len(set(teiki_1) & set(teiki_N)) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
