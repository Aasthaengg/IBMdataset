def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** .5) + 1, 2):
        if x % i == 0:
            return False
    return True
n = int(input())
print(sum(is_prime(int(input())) for _ in range(n)))
