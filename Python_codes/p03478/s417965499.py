def calc_sum_digits(n):
    sumdigit = 0
    while n > 0:
        sumdigit += n % 10
        n //= 10
    return sumdigit

N, A, B = map(int, input().split())
result = 0
for n in range(1, N+1):
    sumdigit = calc_sum_digits(n)
    if sumdigit >= A and sumdigit <= B:
        result += n
print(result)