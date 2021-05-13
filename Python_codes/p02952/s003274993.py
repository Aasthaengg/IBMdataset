# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())

cnt = 0
for index in range(1, n+1):
    digit, _ = calc_digit_sum(index)
    if digit % 2 != 0:
        cnt += 1

print(cnt)