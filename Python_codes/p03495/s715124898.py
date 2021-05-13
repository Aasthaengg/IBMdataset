#!/usr/bin/env python3
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

b = [[a[0],1]]
cnt = 0

for i in a[1:] :
    if b[cnt][0] == i:
        b[cnt][1] += 1
    else:
        b.append([i, 1])
        cnt += 1

num = len(b)
b_sorted = sorted(b, key=lambda x: x[1])

ans = 0
for i, j in b_sorted[: num - k]:
    ans += j

print(ans)
