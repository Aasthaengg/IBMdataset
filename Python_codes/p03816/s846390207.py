import sys
import collections

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    x = 0
    twon = 0
    c = collections.Counter(A)
    for k in c.keys():
        if c[k] >= 2:
            if c[k] % 2 == 0:
                x += c[k] - 2
                twon += 1
            else:
                x += c[k] - 1

    x += twon
    if twon & 1:
        x += 1

    print(N - x)



if __name__ == '__main__':
    main()
