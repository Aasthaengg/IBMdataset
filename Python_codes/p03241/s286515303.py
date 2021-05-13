import sys
from fractions import gcd
def input(): return sys.stdin.readline().strip()


def make_divisors(n):
    divisors = []
    divisors2 = []
    for i in range(1, int(round(n**0.5))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def main():
    N, M = map(int, input().split())
    divisors = make_divisors(M)
    while True:
        d = divisors.pop()
        if M >= N * d:
            print(d)
            return




if __name__ == "__main__":
    main()
