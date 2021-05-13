# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())

answer = 0
for num in range(1, n + 1, 2):
    cnt = 0
    for candidate in range(1, num + 1):
        if num % candidate == 0:
            cnt += 1

    if cnt == 8:
        answer += 1

print(answer)
