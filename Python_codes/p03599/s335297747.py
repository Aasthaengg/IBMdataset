import sys
water1,water2,sugar1,sugar2,per_limit,total_limit = map(int,input().split())

max_sugar_per_water = 0
best_total = 0
best_sugar = 0
# waterはfor使うか、、、

if per_limit == 0:
    print(100*water1)
    sys.exit()

for time_water1 in range(30):
    for time_water2 in range(30):
        water = water1*time_water1*100 + water2*time_water2*100
        if water > total_limit:
            break
        if water == 0:
            continue

        sugar_limit = (water//100)*per_limit
        time_sugar1 = 0
        while True:
            time_sugar2 = 0
            while True:
                sugar = sugar1*time_sugar1+sugar2*time_sugar2

                # トータルの重さ判定
                if total_limit < water+sugar:
                    break
                # 溶ける量制限判定
                if sugar_limit < sugar:
                    break

                # 濃度求めて、最大なら更新
                sugar_per_water = sugar/water
                if sugar_per_water >= max_sugar_per_water:
                    max_sugar_per_water = sugar_per_water
                    best_sugar = sugar
                    best_total = sugar+water

                # 砂糖2の量を更新
                time_sugar2 += 1

            # 砂糖1だけで制限超過してたらbreak
            if sugar1*time_sugar1 > sugar_limit or sugar1*time_sugar1 + water > total_limit:
                break
            # 砂糖1を更新
            time_sugar1 += 1

        if water > total_limit:
            break
print(best_total,best_sugar)