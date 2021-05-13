import sys
import math

def is_prime(num):
    if num < 2: return False
    elif num == 2: return True
    elif num % 2 == 0: return False
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

def call_is_prime(n):
    return [i for i in range(1,n) if is_prime(i)]


def main():
    
    input = sys.stdin.readline
    x = int(input())
    primes = call_is_prime(x+1000)
    ans = [i for i in primes if i>=x]
    print(min(ans))


if __name__ == "__main__":
    main()

