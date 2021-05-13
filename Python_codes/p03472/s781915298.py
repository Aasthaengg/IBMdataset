from math import ceil

N, H = map(int, input().split())
dmg = []
for _ in range(N):
    a, b = map(int, input().split())
    dmg.append(a)
    dmg.append(b)
tl = [(i, d) for i, d in enumerate(dmg)]
tl.sort(key=lambda x: x[1], reverse=True)

ans = 0
rest = H
for i in range(2*N):
    idx, damage = tl[i]
    if idx % 2 == 0:
        if rest % damage == 0:
            ans += rest // damage
        else:
            ans += rest // damage + 1
        break
    else:
        ans += 1
        rest -= damage
        if rest <= 0:
            break
print(ans)