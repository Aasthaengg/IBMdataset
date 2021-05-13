from heapq import heappop, heappush

N,D,A = map(int, input().split())
XH = [[int(i) for i in input().split()] for _ in range(N)]

XH.sort(key=lambda x: x[0])

ans = 0
bomb = []
SUMD = 0 # ダメージの総和
for x, h in XH:
    while bomb:
        right, damage = heappop(bomb)
        if right < x:
            SUMD -= damage
        else:
            heappush(bomb, (right, damage))
            break
    h -= SUMD
    if h > 0:
        cnt = (h + A - 1) // A
        SUMD += cnt * A
        heappush(bomb, (x + 2 * D, cnt * A))
        ans += cnt

print(ans)