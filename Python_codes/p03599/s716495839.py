A, B, C, D, E, F = map(int,input().split())
water = [0 for _ in range(31)]
sugar = [0 for _ in range(3001)]
water[0] = 1
sugar[0] = 1
for i in range(30):
    if water[i] == 0:
        continue
    if i + A <= 30:
        water[i+A] = 1
    if i + B <= 30:
        water[i+B] = 1
for i in range(3000):
    if sugar[i] == 0:
        continue
    if i + C <= 3000:
        sugar[i+C] = 1
    if i + D <= 3000:
        sugar[i+D] = 1

MAX = -1
ans = None
for i in range(1, 31):
    for j in range(3001):
        if water[i] == 0 or sugar[j] == 0 or i * 100 + j > F or i * E < j:
            continue
        if MAX < 100 * j / (j + i * 100):
            MAX = 100 * j / (j + i * 100)
            ans = [i * 100 + j, j]
print(*ans)