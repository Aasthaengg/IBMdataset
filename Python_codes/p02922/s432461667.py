import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    print(math.ceil((b-1)/(a-1)))

if __name__ == '__main__':
    main()