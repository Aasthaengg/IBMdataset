import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from copy import deepcopy

def main():
    n, *x = map(int, read().split())
    if n == 2:
        print(x[1])
        print(x[0])
        sys.exit()

    x2 = deepcopy(x)
    x2.sort()
    r1 = x2[n//2-1]
    r2 = x2[n//2]
    for xe in x:
        if xe > r1:
            print(r1)
        else:
            print(r2)
if __name__ == '__main__':
    main()