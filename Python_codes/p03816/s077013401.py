from collections import defaultdict

N = int(input())
A = sorted(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

ans = 0
duplicate = 0
q = list()
for k, v in d.items():
    if v % 2 == 1:
        d[k] = 1
        ans += 1
    else:
        d[k] = 2
        duplicate += 1

ans += duplicate
if duplicate % 2 == 1:
    ans -= 1

print(ans)
