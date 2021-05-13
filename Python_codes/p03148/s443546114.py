# D - Various Sushi

import sys

N, K = map(int, sys.stdin.buffer.readline().split())
td = []
for _ in range(N):
    tmp1, tmp2 = map(int, sys.stdin.buffer.readline().split())
    td.append([tmp1-1, tmp2, -1])

td = sorted(td, key = lambda x: x[1], reverse = True)
t_counter = [0]*N
for idx in range(N):
    t_counter[td[idx][0]] += 1
    td[idx][2] = t_counter[td[idx][0]]

t_set = set([td[idx][0] for idx in range(K)])
ans_list = []
ans = sum([td[idx][1] for idx in range(K)]) + len(t_set)**2
ans_list.append(ans)

a = 0
b = 0
while 1:
    while K - 1 - a >= 0:
        if td[K - 1 - a][2] >= 2:
            ans -= td[K - 1 - a][1]
            a += 1
            break
        a += 1
    if K-1-a < 0:
        break
    while K + b <= N-1:
        if td[K + b][0] not in t_set:
            ans -= len(t_set)**2
            t_set.add(td[K + b][0])
            ans += td[K + b][1] + len(t_set)**2
            b += 1
            break
        b += 1
    ans_list.append(ans)
    if K+b == N:
        break

print(max(ans_list))