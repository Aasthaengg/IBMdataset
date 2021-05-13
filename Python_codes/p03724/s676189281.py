from collections import defaultdict
N, M = map(int, input().split())
c = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    c[a] += 1
    c[b] += 1

flag = True
for k, v in c.items():
    if v % 2 != 0:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
