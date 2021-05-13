from math import sqrt

def prime_numbers(n):
    total = 0
    for x in n:
        if is_prime(x):
            total += 1
    return total

def is_prime(x):
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False

    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = []
    for _ in range(int(input())):
        n.append(int(input()))
    print(prime_numbers(n))

