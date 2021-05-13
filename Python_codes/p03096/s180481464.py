from collections import defaultdict
mod = 10**9 + 7
n = int(input())
prev = None
s = []
d = defaultdict(list)
cnt = 0
for i in range(n):
    c = int(input())
    if prev == c:
        continue
    prev = c
    s.append(c)
    d[c].append(cnt)
    cnt += 1
#print(s)
DP = [0]*cnt
DP[0] = 1
e = {}
for i, c in enumerate(s):
    if i == cnt-1:
        break
    e[c] = e.get(c, 0) + 1
    j = e[c]
    DP[i+1] = (DP[i+1] + DP[i]) % mod
    if j < len(d[c]):
        DP[d[c][j]] = (DP[d[c][j]] + DP[i]) % mod
    #print(DP)
print(DP[-1])