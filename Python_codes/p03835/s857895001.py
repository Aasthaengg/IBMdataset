# 各桁の数値の総和を計算する.
def calc_digit_sum(num):
    sums = 0
    while num > 0:
        sums += num % 10
        num //= 10
    return sums


k, s = map(int, input().split())

cnt = 0
for idx1 in range(0, k+1):
    for idx2 in range(0, k+1):
        current = s - (idx1 + idx2)
        if 0 <= current <= k:
            cnt += 1

print(cnt)
