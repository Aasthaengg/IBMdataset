import math
def calc(x, y, z):
    return x * x + y * y + z * z + x * y + y * z + z * x

def calc_combination_num(x, y, z):
    if x == y and y == z:
        # 全部同じ数字なら組み合わせの個数は1個
        return 1
    if x == y or y == z:
        # どれか2つが同じ数字なら組み合わせの個数は3C2 = 3個
        return 3
    # 全部違う数字なら組み合わせの個数は3P2 = 6個
    return 6

N = int(input())

result_map = {}
for i in range(1, N + 1):
    result_map[i] = 0

# x <= y <= zとしてループを回し
for x in range(1, N):
    tempFn1 = calc(x, 0, 0)
    if tempFn1 > N:
        # もう数値は増える一方なのでやる必要なし
        break
    for y in range(x, N):
        tempFn2 = calc(x, y, 0)
        if tempFn2 > N:
            # もう数値は増える一方なのでやる必要なし
            break
        for z in range (y, N):
            fn = calc(x, y, z)
            if fn > N:
                # もう数値は増える一方なのでやる必要なし
                break
            # 組み合わせの個数の算出
            combination_num = calc_combination_num(x, y, z)
            result_map[fn] = result_map[fn] + combination_num

for result in result_map.values():
    print(result)
