import sys
 
A, B, C, D, E, F = map(int, sys.stdin.readline().split())
 
max_a = (F - 1) // (100 * A) + 1
max_b = (F - 1) // (100 * B) + 1
 
max_rate = 0
ans_water = 0
ans_sugar = 0
for a in range(max_a + 1):
    for b in range(max_b + 1):
        water = 100 * A * a + 100 * B * b
        if water >= F:
            break
 
        max_sugar = min(F - water, water // 100 * E)
        # print("max_sugar", max_sugar)
        max_c = (max_sugar - 1) // C + 1
        max_d = (max_sugar - 1) // D + 1
        for c in range(max_c + 1):
            for d in range(max_d + 1):
                sugar = C * c + D * d
                if sugar > max_sugar or sugar + water > F:
                    break
 
                if sugar * (ans_water + ans_sugar) >= ans_sugar * (water + sugar):
                    ans_water = water
                    ans_sugar = sugar
 
print(ans_water + ans_sugar, ans_sugar)