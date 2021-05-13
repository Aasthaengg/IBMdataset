import sys
import math
import decimal
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')


def main():
    N = int(readline())
    JPY = 0
    BTC = 0
    for _ in range(N):
        x, u = readline().decode('utf-8').strip().split()
        if u == 'JPY':
            JPY += int(x)
        else:
            BTC += decimal.Decimal(x)

    ans = JPY + BTC*380000
    print(ans)
if __name__ == '__main__':
    main()
