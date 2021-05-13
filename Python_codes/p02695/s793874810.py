n,m,q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(q)]

ans = 0

import itertools
for con in itertools.combinations_with_replacement(list(range(m)), n):
    tmp = 0
    for i in l:
        a,b,c,d = i
        if con[b-1] - con[a-1] == c:
            tmp += d
    ans = max(ans, tmp)

print(ans)
