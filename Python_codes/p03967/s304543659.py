import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    s = in_s()
    N = len(s)

    cnt_g = 0
    cnt_p = 0
    score = 0

    for i in range(N):

        if s[i] == 'g':
            if cnt_p < cnt_g:
                cnt_p += 1
                score += 1
            else:
                cnt_g += 1
        else:
            if cnt_p < cnt_g:
                cnt_p += 1
            else:
                cnt_g += 1
                score -= 1

    print(score)


if __name__ == '__main__':
    main()
