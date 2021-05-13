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

    ans = 0
    ar, br, abr = 0, 0, 0
    for i in range(N):
        s = in_s()
        ans += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A':
            abr += 1
        elif s[0] == 'B':
            br += 1
        elif s[-1] == 'A':
            ar += 1

    # print(ans)
    #print(ar, br, abr)

    t = abr
    if ar > 0:
        ar -= 1
        t += 1
    if br > 0:
        br -= 1
        t += 1
    if t > 1:
        ans += t - 1

    ans += min(ar, br)
    print(ans)


if __name__ == '__main__':
    main()
