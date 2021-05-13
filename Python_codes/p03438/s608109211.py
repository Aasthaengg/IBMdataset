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
    a = in_nl()
    b = in_nl()

    count = sum(b) - sum(a)

    x, y = 0, 0
    for i in range(N):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            y += a[i] - b[i]
        else:
            t = b[i] - a[i]
            if t % 2 == 0:
                x += t // 2
            else:
                x += t // 2 + 1
                y += 1

    if count < 0:
        ans = 'No'
    else:
        if count < x or count < y:
            ans = 'No'
        else:
            if y + 2 * (count - x) == count:
                ans = 'Yes'
            else:
                ans = 'No'

    # print(count)
    #print(x, y)
    print(ans)


if __name__ == '__main__':
    main()
