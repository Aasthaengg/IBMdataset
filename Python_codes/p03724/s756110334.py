n, m = map(int, input().split())

dic = {}

for i in range(m):
    a, b = map(int, input().split())

    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1

ok = 1

for k, v in dic.items():
    if v % 2 != 0:
        ok = 0
        break

print('YES' if ok else 'NO')
