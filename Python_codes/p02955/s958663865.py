import sys
import math

def get_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

def main():
    _, K = map(int, input().split())
    *A, = map(int, input().split())

    aSum = sum(A)
    divs = get_divisor(aSum)

    for d in divs:
        r = [a % d for a in A]
        r.sort()

        sumRm = d*len(r) - sum(r)

        tmpSum = 0
        for _r in r:
            tmpSum += _r
            sumRm = sumRm - (d-_r)
            op = max(tmpSum, sumRm)
            if op <= K:
                print(d)
                sys.exit()

if __name__ == '__main__':
    main()