# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())
s, t = input().split()

answer = ""
for ch1, ch2 in zip(s, t):
    answer += ch1 + ch2

print(answer)