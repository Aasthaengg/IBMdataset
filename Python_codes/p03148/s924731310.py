from heapq import heappush, heappop

N, K = map(int, input().split())
sushi = [[] for _ in range(N+1)]
for _ in range(N):
    t, d = map(int, input().split())
    sushi[t].append(d)
for li in sushi:
    li.sort()

first = [(li[-1], i) for i, li in enumerate(sushi) if li]
first.sort(reverse = True)

kind = 0
v_first = 0
second = []
second_sum = 0
second_cnt = 0

ans = 0
for v, i in first:
    kind += 1
    if kind > K:
        break
    v_first += v
    for d in sushi[i][:-1]:
        heappush(second, d)
        second_sum += d
        second_cnt += 1
    while second_cnt > (K-kind):
        d = heappop(second)
        second_cnt -= 1
        second_sum -= d
    value = kind*kind + v_first + second_sum
    if ans < value:
        ans = value

print(ans)