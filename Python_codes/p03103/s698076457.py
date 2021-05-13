N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])
r = 0
for a, b in AB:
    if M <= 0:
        break
    if b <= M:
        r += a*b
        M -= b
    elif b >= M:
        r += a*M
        break
print(r)
