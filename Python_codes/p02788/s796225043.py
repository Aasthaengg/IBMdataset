from collections import deque

N, D, A = map(int, input().split())
Monsters = [tuple(map(int, input().split())) for _ in range(N)]
Monsters.sort()
Attack = deque()
attack = 0
ans = 0
for x, h in Monsters:
    while Attack and Attack[0][0] <= x:
        y, at = Attack.popleft()
        attack -= at
    h -= attack
    num = max((h - 1) // A + 1, 0)
    attack += num * A
    ans += num
    Attack.append((x + 2 * D + 1, num * A))
print(ans)
