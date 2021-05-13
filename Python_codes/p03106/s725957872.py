# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


cnt = 0
a, b, k = map(int, input().split())
for num in range(max(a, b), -1, -1):
    if a % num == 0 and b % num == 0:
        cnt += 1
        if k == cnt:
            print(num)
            exit()