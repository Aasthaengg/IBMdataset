import sys
from collections import defaultdict

s = list(map(str, input().rstrip()))
k = int(input())
connection = False

if all([x == s[0] for x in s]):
    print(len(s) * k // 2)
    sys.exit()

cnt = 0
if s[0] == s[-1] and k != 1:
    connection = True
    cnt = 2
    start = 1
    goal = 1
    x = s[0]

    for i in s[1:]:
        if i == x:
            cnt += 1
            start += 1
        else:
            break

    for i in s[:-1][::-1]:
        if i == x:
            cnt += 1
            goal += 1
        else:
            break

d = defaultdict(int)

if connection:
    ss = s[:start]
    sg = s[-goal:]
    s = s[start:-goal]
    
prev = s[0]
tmp = 1
for i, x in enumerate(s[1:]):
    if prev == x and i == (len(s) - 2):
        tmp += 1
        d[tmp] += 1
    elif prev == x:
        tmp += 1
    else:
        d[tmp] += 1
        prev = x
        tmp = 1

if connection:
    d[cnt] += 1

ans = 0
for key, val in d.items():
    if key == 1:
        continue
    else:
        ans += key // 2 * val * k

if connection:
    ans -= cnt // 2
    ans += len(ss) // 2 + len(sg) // 2

print(ans)