from collections import Counter
from itertools import accumulate

n, k = map(int, input().split())
aaa = list(map(int, input().split()))
bbb = list(accumulate(aaa))
ccc = list(-i % k for i in range(n))
ddd = [(b + c) % k for b, c in zip(bbb, ccc)]

# print(aaa)
# print(bbb)
# print(ccc)
# print(ddd)

count = dict(Counter(ddd[:k - 1]))
ans = 0
for i in range(n):
    key = (1 - aaa[i] + bbb[i] + ccc[i]) % k
    if key in count:
        ans += count[key]

    j = i + k - 1
    if j < n:
        dj = ddd[j]
        if dj not in count:
            count[dj] = 1
        else:
            count[dj] += 1

    di = ddd[i]
    count[di] -= 1
    if count[di] == 0:
        count.pop(di)

print(ans)
