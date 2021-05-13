import heapq

n, h = [int(i) for i in input().split()]
attack = 0
throw = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    attack = max(a, attack)
    heapq.heappush(throw, -b)

cnt = 0
t = -heapq.heappop(throw)
while h > 0:
    if t > attack:
        h -= t
        cnt += 1
        if throw:
            t = -heapq.heappop(throw)
        else:
            t = -1
    else:
        cnt += h // attack
        if h % attack > 0:
            cnt += 1
        break

print(cnt)
