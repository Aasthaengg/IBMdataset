import sys
N = int(input())
counts = {}
for _ in range(N):
    s = tuple(sorted(sys.stdin.readline()))
    counts[s] = counts.get(s, 0) + 1
ans = 0
for count in counts.values():
    if count > 1:
        ans += (count * (count - 1) // 2)
print(ans)