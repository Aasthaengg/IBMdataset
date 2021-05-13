# 数値の取得
hp,n = map(int,input().split())
damage_list = list(map(int,input().split()))

# 判定結果を出力
damage_sum = sum(damage_list)
if damage_sum >= hp:
    print("Yes")
else:
    print("No")