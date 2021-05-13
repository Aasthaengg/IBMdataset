# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())
arr = map(int, input().split())

candidate = [n for n in arr if n % 2 == 0]
for check in candidate:
    if check % 3 != 0 and check % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
