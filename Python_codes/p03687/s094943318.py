from collections import Counter
s = input()

cnt = Counter(c for c in s)

ans = 100100
for c in cnt.keys():
    len_m = max([len(a) for a in s.split(c)])
    ans = min(ans, len_m)

print(ans)