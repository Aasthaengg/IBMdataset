import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    S = list(in_s())
    N = len(S)
    K = in_n()

    ac = ord('a') + 26
    zc = ord('z')

    for i in range(N):
        if S[i] != 'a':
            nc = ord(S[i])
            if ac - nc <= K:
                S[i] = 'a'
                K -= ac - nc

    if K != 0:
        tc = S[-1]
        S[-1] = chr(((ord(tc) - ord('a')) + K % 26) % 26 + ord('a'))

    print(''.join(S))


if __name__ == '__main__':
    main()
