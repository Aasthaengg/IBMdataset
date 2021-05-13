n, h = map(int,input().split())
throw = []
attack = 0
for _ in range(n):
    a, b = map(int,input().split())
    throw.append(b)
    attack = max(attack, a)
throw.sort(reverse=True)

ans = 0
for t in throw:
    if t > attack:
        ans += 1
        h -= t
        if h <= 0:
            break
    else:
        break
if h > 0:
    ans += -(-h//attack)

print(ans)