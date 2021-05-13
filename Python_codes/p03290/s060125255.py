# https://atcoder.jp/contests/abc104/tasks/abc104_c

from itertools import product
from itertools import compress


D, G = map(int, input().split())
data = []
for _ in range(D):
    data.append(tuple(map(int, input().split())))

res = []
for bit in product(*((0,1),)*D):
    S = 0
    cnt = 0
    for i, a in enumerate(data):
        p, c = a
        S += (100*(i+1)*p + c)*(bit[i]==0)
        cnt += p*(bit[i]==0)
    if S >= G:
        res.append(cnt)
    else:
        for i, d in enumerate(reversed(bit)):
            if d:
                break
        for k in range(1,data[D-i-1][0]+1):
            cnt += 1
            if S + 100*(D-i)*k >= G:
                res.append(cnt)
                break


print(min(res))