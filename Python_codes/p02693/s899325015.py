import sys
import itertools


def resolve(in_):
    k = int(next(in_))
    a, b = map(int, next(in_).split())
    for v in range(a, b + 1):
        if not v % k:
            return 'OK'
    
    return 'NG'


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()