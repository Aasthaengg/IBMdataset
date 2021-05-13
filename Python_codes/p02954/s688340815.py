import math
from itertools import groupby

def rlE(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, (len(list(v)))))
    return res

S = input()
ans = [0 for _ in range(len(S))]
cnt = 0
rS = rlE(S)
rS.append(["", 0])
temp = rS[0][1] - 1

while(cnt < len(rS) - 1):
    ans[temp] = math.ceil(rS[cnt][1] / 2) + rS[cnt + 1][1] - math.ceil(rS[cnt + 1][1] / 2)
    ans[temp + 1] = math.ceil(rS[cnt + 1][1] / 2) + rS[cnt][1] - math.ceil(rS[cnt][1] / 2)
    temp += (rS[cnt + 1][1] + rS[cnt + 2][1])
    cnt += 2
print(*ans)