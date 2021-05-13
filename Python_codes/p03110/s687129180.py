import sys
import math
import bisect

def main():
    ans = 0
    for _ in range(int(input())):
        a, b = input().split()
        a = float(a)
        if b == 'JPY':
            ans += a
        elif b == 'BTC':
            ans += a * 380000
    print('%.10f' % ans)

if __name__ == "__main__":
    main()
