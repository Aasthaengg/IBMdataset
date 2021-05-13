# 各桁の数値の総和を計算する.
def calc_digit_sum(num):
    sums = 0
    while num > 0:
        sums += num % 10
        num //= 10
    return sums


s = input()
contains = set(["A", "C", "G", "T"])

answer = cnt = 0
for ch in s:
    if ch not in contains:
        cnt = 0
    else:
        cnt += 1
    answer = max(answer, cnt)

print(answer)