from collections import defaultdict
a = input()
n = len(a)
d = defaultdict(int)
for i in a:
    d[i] += 1
ans = 1 + n*(n-1)//2
for i in d.values():
    ans -= i*(i-1)//2

print(ans)
