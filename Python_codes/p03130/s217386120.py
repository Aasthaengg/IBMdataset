from collections import defaultdict
cnt = defaultdict(int)
for i in range(3):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

print("YES" if max(cnt.values()) == 2 and min(cnt.values()) == 1 else "NO")