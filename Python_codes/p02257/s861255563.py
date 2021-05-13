from sys import stdin
def isPrime(x):
    if x == 2: return 1
    elif x % 2 == 0: return 0
    return pow(2, x - 1, x) == 1
print(len([0 for _ in range(int(stdin.readline())) if isPrime(int(stdin.readline())) == 1]))