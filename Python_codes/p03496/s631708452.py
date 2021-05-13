#!/usr/bin/env python3
N = int(input())
a = list(map(int, input().split()))

cnt = 0
op = []
mx = {'i':a.index(max(a)), 'v':max(a)}
mn = {'i':a.index(min(a)), 'v':min(a)}
for i in range(N):
    if mx['v'] > 0 and mn['v'] < 0:
        if abs(mx['v']) > abs(mn['v']):
            if a[i] < 0:
                cnt += 1
                op.append([mx['i'] + 1, i + 1])
                a[i] += mx['v']
        else:
            if a[i] > 0:
                cnt += 1
                op.append([mn['i'] + 1, i + 1])
                a[i] += mn['v']

if abs(mx['v']) > abs(mn['v']):
    for i in range(N - 1):
        if a[i] > a[i + 1]:
            cnt += 1
            op.append([i + 1, i + 2])
            a[i + 1] += a[i]
else:
    for i in range(N - 1)[::-1]:
        if a[i] > a[i + 1]:
            cnt += 1
            op.append([i + 2, i + 1])
            a[i] += a[i + 1]

print(cnt)
for i in range(cnt):
    print(op[i][0], op[i][1])
