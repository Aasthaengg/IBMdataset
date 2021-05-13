import sys
import copy
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    A = sorted(in_nl())

    while True:
        B = []
        B.append(A[0])
        for i in range(1, len(A)):
            x = A[i] % A[0]
            if x:
                B.append(x)

        if len(B) == 1:
            break
        else:
            B.sort()
            A = copy.copy(B)

    print(B[0])


if __name__ == '__main__':
    main()
