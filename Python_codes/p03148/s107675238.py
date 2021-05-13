from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

N, K = [int(x) for x in stdin.readline().rstrip().split()]
S = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
d = defaultdict(list)

for i in range(N):
    S[i][0] -= 1
    d[S[i][0]].append(S[i][1])

max_d = [None] * N

for k, v in d.items():
    max_d[k] = max(v)

S.sort(key=lambda x: x[1], reverse=True)
priority_queue1 = []
flag = [0] * N
ans = 0

for ti, di in S[:K]:
    ans += di
    flag[ti] = 1

    if di != max_d[ti]:
        heappush(priority_queue1, di)

syuruisuu = flag.count(1)
ans += syuruisuu ** 2
ans_l = [ans]
priority_queue2 = []

for i in range(N):
    if flag[i] == 0 and max_d[i] != None:
        heappush(priority_queue2, -max_d[i])

while len(priority_queue1) and len(priority_queue2):
    add_sushi = -heappop(priority_queue2)
    remove_sushi = heappop(priority_queue1)
    ans_cand = ans_l[-1] - syuruisuu**2 + (syuruisuu+1)**2 + add_sushi - remove_sushi
    ans_l.append(ans_cand)
    syuruisuu += 1

print(max(ans_l))