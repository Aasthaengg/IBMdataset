# 各桁の数値の総和を計算する.
def calc_digit_sum(num):
    sums = 0
    while num > 0:
        sums += num % 10
        num //= 10
    return sums


n = int(input())
for idx1 in range(1, 10):
    for idx2 in range(1, 10):
        if idx1 * idx2 == n:
            print("Yes")
            exit()

print("No")