import numpy as np
n = int(input())
p = np.array(list(map(int,input().split())))

a = np.arange(1, n+1)
tmp = p - a
cnt = np.count_nonzero(tmp != 0)

flg = False
if cnt == 0 or (cnt == 2 and tmp.sum() == 0):
    flg = True

print('YES') if flg else print('NO')