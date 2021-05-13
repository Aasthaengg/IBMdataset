# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n, m = map(int, input().split())
arr = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    arr.append(tmp[1:])
prr = list(map(int, input().split()))

answer = 0
for switches in range(2 ** n):
    light_up = 0
    for light in range(m):
        on = 0
        for shift in range(n):
            if (switches >> shift) & 1 and (shift + 1) in arr[light]:
                on += 1

        if on % 2 == prr[light]:
            light_up += 1

    if light_up == m:
        answer += 1

print(answer)