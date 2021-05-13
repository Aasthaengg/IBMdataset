from collections import defaultdict
N = int(input())
D = [int(x) for x in input().split()]
M = int(input())
T = [int(x) for x in input().split()]

cnt = defaultdict(int)
for d in D:
    cnt[d] += 1
for t in T:
    cnt[t] -= 1

if min(cnt.values()) >= 0:
    print('YES')
else:
    print('NO')

