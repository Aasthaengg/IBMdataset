import math


def is_prime(num):
    if num == 2:
        return True
    elif not num & 1:
        return False

    for i in range(3, math.ceil(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


N = int(input())
nums = [int(input()) for _ in range(N)]
ans = len([num for num in nums if is_prime(num)])
print(ans)