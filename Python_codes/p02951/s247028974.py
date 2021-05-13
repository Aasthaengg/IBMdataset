# 数値を取得
max_c1,wat_c1,wat_c2 = map(int,input().split())

# 容器2の残量を出力
able_wat = max_c1 - wat_c1
remain_c2 = max(wat_c2 - able_wat,0)
print(remain_c2)