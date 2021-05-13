
import sys
read = sys.stdin.read
from math import sqrt, ceil
def main():
    n, m = map(int, input().split())
    if n == 1:
        print(m)
        sys.exit()

    divs = []
    for i1 in range(2, ceil(sqrt(m))+1):
        if m % i1 == 0:
            divs.append(i1)
            divs.append(int(m/i1))
    divs.sort()
    r = 1
    for div in divs:
        if n * div <= m:
            r = div
        else:
            break
    print(r)

if __name__ == '__main__':
    main()