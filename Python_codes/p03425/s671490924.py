from itertools import combinations
N = int(input())
dic = {}
for _ in range(N):
    x = list(input())[0]
    if x in ("M", "A", "R", "C", "H"):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
ans = 0
comb = list(combinations(dic.keys(), 3))
for x, y, z in comb:
    ans += dic[x] * dic[y] * dic[z]
print(ans)