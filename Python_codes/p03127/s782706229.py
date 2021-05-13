from functools import reduce
import math
def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(reduce(math.gcd, A))

if __name__ == '__main__':
    main()
