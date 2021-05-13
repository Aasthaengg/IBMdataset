N, H = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

ans = 0
attack = []

for a, b in ab:
    attack += [[a, 0]]
    attack += [[b, 1]]

attack = sorted(attack, key=lambda x:(-x[0], x[1]))

for a, i in attack:
    if i == 1:
        H -= a
        ans += 1
        if H <= 0:
            break
    else:
        cnt = (H-1)//a + 1
        ans += cnt
        break

print(ans)