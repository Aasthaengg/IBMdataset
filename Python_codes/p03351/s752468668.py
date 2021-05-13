# A - Colorful Transceivers
# A さんと C さんが会話できるなら　YES!!!!
# 条件1： A さんと C さんの距離が d 以下
# 条件2： A さんと B さんの距離が d 以下　∧ B さんと C さんの距離が d 以下


# A さん a [m]
# B さん b [m]
# C さん c [m]
# D さん d [m]

# 標準入力 a b c d
a, b, c, d = map(int, input().split(maxsplit=4))
# print(a)
# print(b)
# print(c)
# print(d)


# A さんと C さんの距離を計算
distance_ac = abs(a - c)
# print(distance_ac)

# A さんと B さんの距離を計算
distance_ab = abs(a - b)
# print(distance_ab)

# B さんと C さんの距離を計算
distance_bc = abs(b - c)
# print(distance_bc)

# 条件1 条件2に分けて Yes No を代入
if distance_ac <= d:    # 条件1
    # print('Yes')
    answer = 'Yes'
elif distance_ab <= d:  # 条件2
    if distance_bc <= d:
        # print('Yes')
        answer = 'Yes'
    else:
        # print('No')
        answer = 'No'
else:
    # print('No')
    answer = 'No'

# 結果の出力
print(answer)