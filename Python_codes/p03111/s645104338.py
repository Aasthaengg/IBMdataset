n, a, b, c = map(int, input().split())
T = [a, b, c]
L = [int(input()) for _ in range(n)]

import itertools
ans = 10**18
for p in itertools.product(range(4), repeat=n):
    C = [0]*3
    temp = [0]*3
    for i in range(n):
        if p[i] == 3:
            continue
        C[p[i]] += 1
        temp[p[i]] += L[i]
    flag = True
    for i in range(3):
        if C[i] == 0:
            flag = False
            break
    if not flag:
        continue
    mp = 0
    for i in range(3):
        mp += 10*(C[i]-1)
        mp += abs(temp[i]-T[i])
    ans = min(ans, mp)
print(ans)
