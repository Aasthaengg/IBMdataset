import collections
Sls = list(input())
counter = collections.Counter(Sls)
ans = 'yes'
for i in counter.values():
    if i > 1:
        ans = 'no'
        break
print(ans)