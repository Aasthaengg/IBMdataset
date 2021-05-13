from bisect import bisect

s = list(input())
n = len(s)

r_idx = []
l_idx = []
ans = [0 for x in range(n)]

for i in range(n):
    if s[i] == 'R':
        r_idx.append(i)
    else:
        l_idx.append(i)

for r in r_idx:
    idx = bisect(l_idx, r)
    dist = l_idx[idx] - r
    if dist % 2 == 0:
        ans[l_idx[idx]] += 1
    else:
        ans[l_idx[idx]-1] += 1

for l in l_idx:
    idx = bisect(r_idx, l) - 1
    dist = l - r_idx[idx]
    if dist % 2 == 0:
        ans[r_idx[idx]] += 1
    else:
        ans[r_idx[idx]+1] += 1

print(*ans)
