# https://atcoder.jp/contests/agc014/tasks/agc014_b

from collections import defaultdict

n, m = map(int, input().split())
counter = defaultdict(int)
for _ in range(m):
    ai, bi = map(int, input().split())
    counter[ai] += 1
    counter[bi] += 1


for key in counter:
    if counter[key] % 2 != 0:
        print("NO")
        exit()
else:
    print("YES")