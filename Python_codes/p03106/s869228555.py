import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    A, B, K = in_nn()

    count = 0
    num = min(A, B) + 1
    while count < K:
        num -= 1
        if A % num == 0 and B % num == 0:
            count += 1

    print(num)


if __name__ == '__main__':
    main()
