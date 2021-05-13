from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
s_l = []
for i in range(q):
    s = list(map(int, input().split()))
    s_l.append(s)

ans = 0
for v in combinations_with_replacement(range(1, m+1), n):
    cnt = 0
    for i in range(q):
        if v[s_l[i][1] - 1] - v[s_l[i][0] - 1] == s_l[i][2]:
            cnt += s_l[i][3]
    ans = max(ans, cnt)

print(ans)