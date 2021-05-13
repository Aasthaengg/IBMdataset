import heapq, sys
input = sys.stdin.readline
n, q = map(int, input().split())
event = []
for _ in range(n):
    s, t, x = map(int, input().split())
    event.append((s-x, 1, x))
    event.append((t-x, -1, x))

for _ in range(q):
    d = int(input())
    event.append((d, 2, 0))

event.sort(key=lambda x: (x[0], x[1]))
now = []
memo = set()

tmp = 0

for i, (t, flg, x) in enumerate(event):
    if flg == -1:
        memo.remove(x)
    elif flg == 1:
        heapq.heappush(now, x)
        memo.add(x)
    else:
        while len(now) > 0 and now[0] not in memo:
            heapq.heappop(now)
        if len(now) > 0:
            print(now[0])
        else:
            print(-1)