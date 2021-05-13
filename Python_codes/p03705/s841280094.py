import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, a, b = map(int, input().split())
    if (a > b) or (n==1 and a<b):
        print(0)
    elif n == 1 and a == b:
        print(1)
    else:
        print(n*(b-a)+2*(a-b)+1)
            
if __name__ == '__main__':
    main()
