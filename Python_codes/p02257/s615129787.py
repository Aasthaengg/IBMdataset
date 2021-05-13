def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

count = 0

number = int(input())
for i in range(number):
    n = int(input())
    if is_prime(n):
        count = count + 1

print(count)