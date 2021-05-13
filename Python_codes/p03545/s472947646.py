import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import product
def main():
    a, b, c, d = list(input())
    ops = tuple(product(('+', '-'), repeat=3))
    for opse in ops:
        o = a + opse[0] + b + opse[1] + c + opse[2] + d
        s = eval(o)
        if s == 7:
            r = o + '=7'
            print(r)
            sys.exit()

if __name__ == '__main__':
    main()