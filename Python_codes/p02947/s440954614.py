import collections

n = int(input())
s = [''.join(sorted(list(input()))) for _ in range(n)]
s = collections.Counter(s)

ans = 0
for v in s.values():
    ans += v * (v - 1) // 2
print(ans)