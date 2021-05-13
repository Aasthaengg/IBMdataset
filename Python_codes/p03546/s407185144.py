#!/usr/bin/env python3
h, w = map(int, input().split())
c = [[] for _ in range(10)]
cnt = [0] * 10
for i in range(10):
    c[i] = list(map(int, input().split()))
a = [[] for _ in range(h)]
for i in range(h):
    a[i] = list(map(int, input().split()))
    for j in range(10):
        cnt[j] += a[i].count(j)
visit = [0] * 10
val = [c[i][1] for i in range(10)]
visit[1] = 1
pos = 1
while sum(visit) < 10:
    tmp = 10 ** 5  # INF
    for i in range(10):
        if not visit[i]:
            val[i] = min(val[i], val[pos] + c[i][pos])
            if tmp > val[i]:
                # pos = i#ここを更新したらあかんやん。。。
                next_pos = i
                tmp = val[i]
    pos = next_pos
    visit[pos] = 1
ans = 0
# print(val)
for i in range(10):
    ans += val[i] * cnt[i]
print(ans)
