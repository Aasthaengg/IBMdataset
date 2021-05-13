from collections import defaultdict
a, b, c = map(int, input().split())
cnt = defaultdict(int)
cnt[a] += 1
cnt[b] += 1
cnt[c] += 1
print(len(cnt))