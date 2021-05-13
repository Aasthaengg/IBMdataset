arr = list(map(int, input().split()))

max_v = max(arr)
sum_arr = sum(arr)

if (max_v*3 - sum_arr) % 2:
    # 奇数の場合
    print(((max_v+1)*3 - sum_arr) // 2)
else:
    # 偶数の場合
    print((max_v*3 - sum_arr) // 2)