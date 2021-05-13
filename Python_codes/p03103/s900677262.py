N, M = map(int, input().split())

AB = sorted([list(map(int, input().split())) for _ in range(N)])

ans = 0
honsu = 0

for a, b in AB:
    if M - honsu > b:
        ans += a * b
        honsu += b
    else:
        ans += a * (M - honsu)
        honsu += M - honsu
    if M == honsu:
        break

print(ans)
