n = int(input())
s = input()

ans = 0

for i in range(1000):
    # 確認するpinの数字の組み合わせと桁の初期化
    current_digit = 0
    pin = f'{i:0>3}'
    # pin = list(str(i).zfill(3))
    k = pin[current_digit]

    for num in s:
        # 見つけると桁を右に一つずらす
        if num == k:
            current_digit += 1
            # indexが3(桁が3→2→1→0)になったときはそのPINは作れる
            if current_digit <= 2:
                k = pin[current_digit]

            elif current_digit == 3:
                ans += 1
                break

print(ans)