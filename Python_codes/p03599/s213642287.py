A, B, C, D, E, F = map(int, input().split())

# 可能な水の総量
water_list = []
A_max = F // (100 * A)
B_max = F // (100 * B)
for i in range(A_max + 1):
    for j in range(B_max + 1):
        temp = 100 * A * i + 100 * B * j
        if temp <= F:
            water_list.append(temp)
water_list = list(set(water_list))

# 可能な砂糖の総量
sugar_list = []
C_max = F // (C)
D_max = F // (D)
for i in range(C_max + 1):
    for j in range(D_max + 1):
        temp = C * i + D * j
        if temp <= F:
            sugar_list.append(temp)
sugar_list = list(set(sugar_list))

# max_conc=0から始めると0%の場合を拾えなくなる. あるいは34行目で等号をつけても良い.
max_conc = -1
max_conc_water = -1
max_conc_sugar = -1
for water in water_list:
    for sugar in sugar_list:
        # 水があるか and 溶解度を超えていないか and 容器に入るか
        if water != 0 and sugar <= ((E * water) / 100) and water + sugar <= F:
            conc = (100 * sugar) / (water + sugar)
            if conc > max_conc:
                max_conc = conc
                max_conc_water = water
                max_conc_sugar = sugar

print(max_conc_water + max_conc_sugar, max_conc_sugar)
# print(max_conc)
