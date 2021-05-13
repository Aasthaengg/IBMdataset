import numpy as np

MOD = 10**9+7

N = int(input())
DP = [{} for i in range(N+1)]

out = []
AGCT = []
for i in "AGCT":
    for j in "AGCT":
        for k in "AGCT":
            for l in "AGCT":
                str = [i,j,k,l]
                AGCT.append(''.join(str))
                if ''.join(str).count("AGC") >= 1:
                    out.append(''.join(str))
                    continue
                for x  in range(3):
                    hoge = str.copy()
                    hoge[x], hoge[x+1] = hoge[x+1], hoge[x]
                    if ''.join(hoge).count("AGC") >= 1:
                        out.append(''.join(str))
                        break
DP[0]["TTTT"] = 1
for i in range(N):
    for key in AGCT:
        DP[i+1][key] = 0
    for key in DP[i]:
        for c in "AGCT":
            DP[i+1][(key+c)[-4:]] += DP[i][key]
            DP[i+1][(key+c)[-4:]] %= MOD
    for key in out:
        DP[i+1][key] = 0
ans = 0
for i in DP[-1]:
    ans += DP[-1][i]
    ans %= MOD
print(ans)
