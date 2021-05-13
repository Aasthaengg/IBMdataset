n = int(input())
a = 0
b = n
total = []

def digitSum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

for i in range(1, n + 1):
    a = i
    b = n - a
    if b < a:
        break
    total.append(digitSum(a) + digitSum(b))
print(min(total))