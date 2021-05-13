from typing import Counter


n = int(input())
nlis = list(map(int, input().split()))
m = int(input())
mlis = list(map(int, input().split()))

nc  =Counter(nlis)
mc = Counter(mlis)

flag = 1
for k, v in mc.items():
    if mc[k] > nc[k]:
        flag = 0
        break

if flag:
    print('YES')
else:
    print('NO')
