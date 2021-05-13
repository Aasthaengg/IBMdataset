A, B, C, D, E, F = map(int, input().split())
Con = 0
a, b = 0, 0
for i in range(F//100 + 1):
    for j in range(F//100 + 1):
        Water = 100 * A * i + 100 * B * j
        if Water > F:
            break
        for x in range(E * Water // 100 + 1):
            for y in range(E * Water // 100 + 1):
                Sugar = C * x + D * y
                if Water + Sugar > F:
                    break
                if Water * E < Sugar * 100:
                    break
                if Sugar + Water == 0:
                    break
                c = (100 * Sugar) / (Sugar + Water)
                if Con <= c:
                    Con = c
                    a = Water
                    b = Sugar
print(a + b, b)