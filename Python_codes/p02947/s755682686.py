from collections import defaultdict
N = int(input())

d = defaultdict(int)
for i in range(N):
    s = ''.join(sorted(input()))
    d[s] += 1

ans = 0
for c in d.values():
    if c > 1:
        ans += c*(c-1)//2

print(ans)