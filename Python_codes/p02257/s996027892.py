def isPrime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    sqrtnum = num ** 0.5
    for i in range(3, int(sqrtnum + 1), 2):
        if num % i == 0:
            return False
    return True


def prime_number():
    n = int(input())
    count = 0
    for _ in range(n):
        a = int(input())
        if isPrime(a):
            count += 1
    print(count)

if __name__ == "__main__":
    prime_number()