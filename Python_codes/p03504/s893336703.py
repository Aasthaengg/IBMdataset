import numpy as np
n, C = map(int,input().split())
cha = [[0] for _ in range(C+1)]
stc = [list(map(int, input().split())) for _ in range(n)]
stc.sort()
result = np.zeros(2*10**5)
for s, t, c in stc:
    if cha[c] == s:
        result[2*s+1:2*t] += 1
    else:
        result[2*s-1:2*t] += 1
    cha[c] = t
print(int(max(result)))