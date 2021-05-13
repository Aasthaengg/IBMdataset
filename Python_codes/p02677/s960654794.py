import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import radians, cos, sqrt
def main():
    a, b, h, m = map(int, input().split())

    jishin_degree = h * 30 + m * 0.5
    bushin_degree = m * 6
    kakudo = abs(jishin_degree - bushin_degree)

    r = sqrt(a**2 + b**2 - 2 * a * b * cos(radians(kakudo)))
    print(r)

if __name__ == '__main__':
    main()