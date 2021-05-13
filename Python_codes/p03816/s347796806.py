from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    d[i] += 1
cnt = 0
ans = 0
for k, v in d.items():
    if v != 1:
        cnt += v - 1
    ans += 1

if cnt == 0:
    print(ans)
elif cnt == 1:
    print(ans - 1)
elif cnt % 2 == 0:
    print(ans)
else:
    print(ans - 1)