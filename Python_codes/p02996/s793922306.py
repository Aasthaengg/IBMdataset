import sys

read = sys.stdin.buffer.read


def main():
    N, *AB = map(int, read().split())
    T = [0] * N
    for i, (a, b) in enumerate(zip(AB[::2], AB[1::2])):
        T[i] = [b, a]

    T.sort()

    ok = True
    sum_a = 0
    for b, a in T:
        sum_a += a
        if sum_a > b:
            ok = False
            break

    if ok:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
