import math
from functools import reduce

def gcd(numbers):
    return reduce(math.gcd, numbers)

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = gcd(sorted(A,reverse=True))
    print(ans)

if __name__ == '__main__':
    main()