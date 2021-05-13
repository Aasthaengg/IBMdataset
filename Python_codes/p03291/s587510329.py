from collections import Counter


MOD = 10 ** 9 + 7
S = input()
N = len(S)

cnt = Counter()

for s in S:
    if s == 'B':
        cnt['?B'] += cnt['?']
        cnt['AB'] += cnt['A']
    elif s == 'C':
        cnt['ABC'] += cnt['AB']
        cnt['A?C'] += cnt['A?']
        cnt['?BC'] += cnt['?B']
        cnt['??C'] += cnt['??']
    elif s == '?':
        for t in ['??', 'A?', '?B', 'AB']:
            cnt[t + '?'] += cnt[t]
        for t in ['A', '?']:
            cnt[t + '?'] += cnt[t]
    cnt[s] += 1

q = cnt['?']
ans = 0
for key in [x for x in list(cnt.keys()) if len(x) == 3]:
    if cnt[key]:
        ans += cnt[key] * pow(3, q - key.count('?'), MOD)
        ans %= MOD

print(ans)
