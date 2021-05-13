def dfs(num, lst, d, f, cnt):
    if d[num] != 0:
        return cnt - 1
    d[num] = cnt
    for n in lst[num]:
        cnt += 1
        cnt = dfs(n - 1, lst, d, f ,cnt)
    cnt += 1
    f[num] = cnt
    return cnt


n = int(input())
d = [0 for i in range(n)]
f = [0 for i in range(n)]
lst = []
for _ in range(n):
    n = list(map(int, input().split()))
    lst.append(n[2:])

cnt = 1
while 0 in d:
    num = d.index(0)
    cnt = dfs(num, lst, d, f, cnt) + 1

for i, j in enumerate(zip(d, f)):
    print(i + 1, j[0], j[1])
