def is_prime(n):
    if n == 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

x = int(input())
while not is_prime(x):
    x += 1
print(x)