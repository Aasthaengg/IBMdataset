import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, n = map(int, input().split())
    if n < b:
        print(math.floor(a*n/b)-a*math.floor(n/b))
    else:
        print(math.floor(a*(b-1)/b))
    
if __name__ == '__main__':
    main()