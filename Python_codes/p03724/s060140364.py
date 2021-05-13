from collections import defaultdict
N, M = map(int, input().split())
count = defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1
flag = True
for k, v in count.items():
    if v % 2 == 1:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
