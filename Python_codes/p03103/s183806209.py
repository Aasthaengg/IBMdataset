N, M = map(int, input().split())
shops = sorted([list(map(int, input().split())) for _ in range(N)])

total = 0
for shop in shops:
    if M != 0:
        if shop[1] <= M:
            total += shop[0] * shop[1]
            M -= shop[1]
        else:
            total += shop[0] * M
            M = 0
    else:
        break

print(total)