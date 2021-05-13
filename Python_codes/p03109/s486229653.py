import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    S = in_s()
    date = int(S[0:4] + S[5:7] + S[8:])
    if date <= 20190430:
        ans = 'Heisei'
    else:
        ans = 'TBD'

    print(ans)


if __name__ == '__main__':
    main()
