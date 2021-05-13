n = int(input())
total=10*100

def sum_digits(num):
    sum = 0
    while True:
        if num == 0:
            break
        sum += num%10
        num //= 10
    return sum

for a in range(1, n):
    b = n - a
    total = min(total, sum_digits(a)+sum_digits(b))

print(total)
