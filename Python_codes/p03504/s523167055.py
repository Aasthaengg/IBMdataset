import numpy as np
n, C = map(int,input().split())
cha = [[[0,0]] for _ in range(C+1)]
stc = [list(map(int, input().split())) for _ in range(n)]
stc.sort()
for s, t, c in stc:
    if cha[c][-1][1]==s:
        cha[c][-1][1] = t
    else:
        cha[c].append([s, t])
result = np.zeros(2*10**5)
for i in range(1, C+1):
    for s, t in cha[i]:
        result[s*2-1:t*2] += 1
print(int(max(result)))