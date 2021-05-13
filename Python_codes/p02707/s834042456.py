import collections
N = int(input())
A = [int(_) for _ in input().split()]
cnt = collections.defaultdict(int)
for a in A:
    cnt[a] += 1
for i in range(1, N + 1):
    print(cnt[i])
