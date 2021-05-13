S = list(input())
k = int(input())

alp = list('abcdefghijklmnopqrstuvwxyz')
s2a = {alp[i]: 26-i for i in range(26)}
s2a['a'] = 0

for i in range(len(S)):
    s = S[i]
    if s2a[s] <= k:
        k -= s2a[s]
        S[i] = 'a'

k %= 26
idx = alp.index(S[-1])
S[-1] = alp[k+idx]

print(*S, sep='')
