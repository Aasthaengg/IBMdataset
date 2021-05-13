n = int(input())
lis = []
for i in range(2 ** 10):
    openls = []
    for j in range(10):
        if ((i >> j) & 1) == 1:
            openls.append(j)
    lis.append(openls)

f = []
for i in range(n):
    tmp = list(map(int, input().split()))
    f.append(tmp)

p = []
for i in range(n):
    tmp = list(map(int, input().split()))
    p.append(tmp)

ret = - 10 ** 1000

for item in lis:
    if sum(item) == 0:
        continue
    tmp = 0
    for i in range(n):
        same = 0
        for val in item:
            if f[i][val] == 1:
                same += 1
        tmp += p[i][same]
    ret = max(ret, tmp)

print(ret)
