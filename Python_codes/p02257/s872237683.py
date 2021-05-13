import math
n = int(raw_input())
N = []
for i in xrange(n):
    N.append(int(raw_input()))

def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2

    return True

def main():
    cnt = 0
    for x in N:
        if isPrime(x):
            cnt += 1
    print cnt

    return 0

main()