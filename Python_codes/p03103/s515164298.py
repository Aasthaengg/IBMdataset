import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

input_n = lambda: int(readline())
input_nn = lambda: map(int, readline().split())
input_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, M = input_nn()
    AB = sorted([list(input_nn()) for _ in range(N)])

    m = M
    ans = 0
    for i in range(N):
        if AB[i][1] < m:
            ans += AB[i][0] * AB[i][1]
            m -= AB[i][1]
        else:
            ans += AB[i][0] * m
            break

    print(ans)


if __name__ == '__main__':
    main()
