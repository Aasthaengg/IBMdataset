from bisect import bisect_right

def div_ceil(x, y): return (x + y - 1) // y

N, D, A = map(int, input().split())
monsters = [list(map(int, input().split())) for _ in range(N)]
monsters = sorted(monsters, key=lambda x: x[0])
position = [x for x, _ in monsters]
damage = [0] * (N+2)
ans = 0
for i, [x, hp] in enumerate(monsters, 1):
    damage[i] += damage[i-1]
    if damage[i] >= hp: continue
    hp -= damage[i]
    j = bisect_right(position, x + 2*D) + 1
    attack = div_ceil(hp, A)
    ans += attack
    dam = attack * A
    # imos's method
    damage[i] += dam
    damage[j] -= dam
print(ans)