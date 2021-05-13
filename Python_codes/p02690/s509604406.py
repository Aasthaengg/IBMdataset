import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
#import numpy as np
from itertools import product
def main():
    x = int(input())
    n5 = [i**5 for i in range(201)]

    c = product(n5, repeat=2)
    for ce in c:
        if ce[0] + ce[1] == x:
            r = (int(ce[0]**0.2), int(ce[1]**0.2)* -1)
            break
        elif ce[0] - ce[1] == x:
            r = (int(ce[0] ** 0.2), int(ce[1] ** 0.2))
            break
    print(*r, sep=' ')

if __name__ == '__main__':
    main()
