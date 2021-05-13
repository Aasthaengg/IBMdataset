from math import sqrt
def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    x = int(input())
    while not isPrime(x):
        x += 1
    print(x)

if __name__ == "__main__":
    main()
