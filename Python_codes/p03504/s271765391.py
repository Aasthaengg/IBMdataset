import sys
input = sys.stdin.readline

N, C = [int(x) for x in input().split()]
imos = [0]*(10**6 + 2)
stc = [[] for _ in range(31)]
for _ in range(N):
    tmp = [int(x) for x in input().split()]
    stc[tmp[2]].append([tmp[0], tmp[1]])

for i in range(C + 1):
    if len(stc[i]) == 0:
        continue
    stc[i].sort()
    s, t = stc[i][0][0], stc[i][0][1]
    new_stc_i = []
    flag = 1
    for j in range(1, len(stc[i])):
        flag = 0
        if t == stc[i][j][0]:
            t = stc[i][j][1]
            flag = 1
        else:
            new_stc_i.append([s, t])
            s = stc[i][j][0]
            t = stc[i][j][1]
    if flag:
        new_stc_i.append([s, t])
    stc[i] = new_stc_i

for i in range(C + 1):
    stc_i = stc[i]
    for j in stc_i:
        s, t = j 
        s *= 10
        t *= 10
        imos[max(0, s - 5)] += 1
        imos[t] -= 1

from itertools import accumulate

csum = list(accumulate(imos))

print(max(csum))