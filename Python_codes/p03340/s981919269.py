import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    A = in_nl()

    A_sum = [0] * (N + 1)
    A_xor = [0] * (N + 1)

    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
        A_xor[i + 1] = A_xor[i] ^ A[i]

    count = 0
    r = 0
    for l in range(N):
        while r < N:
            #print(l, r, A_sum[r + 1] - A_sum[l], A_xor[r + 1] ^ A_xor[l])
            if A_sum[r + 1] - A_sum[l] == A_xor[r + 1] ^ A_xor[l]:
                r += 1
            else:
                break
        count += r - l
        if r == l:
            r += 1

    print(count)


if __name__ == '__main__':
    main()
