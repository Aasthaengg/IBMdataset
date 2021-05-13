# import sys
# input = sys.stdin.readline


def solve():
    N = int(input())
    brackets_gen = (input() for _ in range(N))

    grads_positive = list()
    grads_negative = list()

    total = 0
    for brackets in brackets_gen:

        elevation, bottom = 0, 0

        for bk in brackets:

            elevation += 1 if bk == '(' else -1
            bottom = min(bottom, elevation)

        if elevation >= 0:
            grads_positive.append((bottom, elevation))
        elif elevation < 0:
            grads_negative.append((bottom - elevation, -elevation))

        total += elevation

    if total != 0:
        return False

    grads_positive.sort(reverse=True)
    grads_negative.sort(reverse=True)

    def is_good(grads):
        elevation, bottom = 0, 0
        for grad in grads:
            bottom = elevation + grad[0]
            if bottom < 0:
                return False
            elevation += grad[1]

        return True

    if is_good(grads_positive) and is_good(grads_negative):
        return True
    else:
        return False


def main():
    ok = solve()
    if ok:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
