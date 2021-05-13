n, a, b = map(int, input().split())

def calc_digit_sum(num):
    sums = 0
    while num > 0:
        sums += num % 10
        num //= 10
    return sums

answer = 0
for num in range(1, n+1):
    sums = calc_digit_sum(num)
    if a <= sums <= b:
        answer += num

print(answer)