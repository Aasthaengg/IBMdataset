import sys
import math

def main():
    N = int(input())
    digit = int(math.log10(N))
    c = N // (10**digit)
    if N < int(str(c) + '9'*digit):
        print(9 * digit + c -1)
    else:
        print(9 * digit + c)

if __name__ == '__main__':
    main()
