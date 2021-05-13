def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
nums = [int(input()) for _ in range(n)]
print(sum(map(is_prime, nums)))