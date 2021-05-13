from heapq import *

N, M = list(map(int, input().split()))
sushi = []
for _ in range(N):
    t, d = list(map(int, input().split()))
    sushi.append([t, d])
sushi.sort(key=lambda x: x[1], reverse=True)

num_sushi = {}
tmp = 0
f = [0] * (N+1)
h = []
for i in range(M):
    s = sushi[i]
    if s[0] in num_sushi:
        num_sushi[s[0]] += 1
    else:
        num_sushi[s[0]] = 1
    heappush(h, (s[1], s[0]))
    tmp += s[1]

f[len(num_sushi)] = tmp

for i in range(M, N):
    if sushi[i][0] in num_sushi:
        continue
    while len(h) > 0:
        s = heappop(h)
        if num_sushi[s[1]] >= 2:
            num_sushi[s[1]] -= 1
            heappush(h, (sushi[i][1], sushi[i][0]))
            num_sushi[sushi[i][0]] = 1
            f[len(num_sushi)] = f[len(num_sushi)-1] + sushi[i][1] - s[0]
            break

ans = 0
for i, g in enumerate(f):
    if g <= 0: continue
    if g + i*i > ans:
        ans = g + i*i
print(ans)
