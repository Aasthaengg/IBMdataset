n, a, b = map(int, input().split())

result = 0
for i in range(1, n + 1):
    number = i
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += (number % 10)
        number //= 10
    if a <= sum_of_digits <= b:
        result += i

print(result)