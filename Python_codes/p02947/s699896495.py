from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

sort_s = []
for s in S:
    sort_s.append(''.join(sorted(s)))

count = dict(Counter(sort_s))

ans = 0
for i in count.values():
    ans += i*(i-1)/2

print(int(ans))
