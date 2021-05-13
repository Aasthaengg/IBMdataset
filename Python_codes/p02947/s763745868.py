from collections import Counter, defaultdict
N = int(input())
d = defaultdict(int)
ans = 0
for i in range(N):
    l = list(input())
    l.sort()
    l = ''.join(l)
    d[l] += 1
for x in d.values():
    ans += x*(x-1)//2
print(ans)