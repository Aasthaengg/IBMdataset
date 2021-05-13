import math
import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    x = 1
    y = n
    for i in range(int(math.sqrt(n)), 0, -1):
        if n%i == 0:
            x = i
            y = n//i
            break
    ans = x + y -2
    print(ans)

if __name__ == '__main__':
    main()