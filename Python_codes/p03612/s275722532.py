import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
ind = list(range(1, n + 1))
tmp = []
for i, j in zip(p, ind):
    if i == j:
        tmp.append(i)
count = 0
ans = 0
for ii, i in enumerate(p):
    if count >= len(tmp):
        break
    if i == tmp[count]:
        ans += 1
        count += 1
        if ii > len(p) - 1 or count > len(tmp)-1:
            break
        # print(ii, count)
        if p[ii + 1] == tmp[count]:
            count = count + 1
print(ans)
