import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import pi
def main():
    R = int(input())
    r = 2 * R * pi
    print(r)

if __name__ == '__main__':
    main()