from collections import Counter
N, K = map(int, input().split())

cnt = Counter()
for _ in range(N):
    a, b = map(int, input().split())
    cnt[a] += b

x = list(cnt.items())
x.sort()

now = 0
for k, v in x:
    now += v
    if K <= now:
        print(k)
        break