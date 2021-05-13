from itertools import permutations

ways = [tuple(map(int, input().split())) for _ in range(3)]
for p in permutations(ways, 3):
    path1 = [p[0][0], p[0][1]]; path2 = [p[0][1], p[0][0]]
    for i in range(1, 3):
        if path1[-1] in p[i]:
            a, b = p[i]; path1.append(a if path1[-1] == b else b)
        if path2[-1] in p[i]:
            a, b = p[i]; path2.append(a if path2[-1] == b else b)
    if max(len(path1), len(path2)) == 4: print('YES'); break;
else: print('NO')