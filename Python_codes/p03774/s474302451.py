n, m = map(int, input().split())
crd_std = []
crd_chk = []
ans = []

for _ in range(n):
    crd_std.append(list(map(int, input().split())))

for _ in range(m):
    crd_chk.append(list(map(int, input().split())))

for s in crd_std:
    min_crd = 10**9
    ans_crd_idx = 100
    for c in range(len(crd_chk)):
        if abs(s[0] - crd_chk[c][0]) + abs(s[1] - crd_chk[c][1]) < min_crd:
            min_crd = abs(s[0] - crd_chk[c][0]) + abs(s[1] - crd_chk[c][1])
            ans_crd_idx = c+1
    ans.append(ans_crd_idx)

for i in ans:
    print(i)
