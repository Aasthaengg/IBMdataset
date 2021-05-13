import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    D = [A[i + 1] - A[i] for i in range(n - 1)]

    for d in D:
        if d != 0:
            if d > 0:
                state = 1
            else:
                state = -1
            break
    else:
        print(1)
        return

    ans = 1
    cnt = 0

    for d in D:
        if d > 0:
            c_state = 1
            cnt += 1
        elif d < 0:
            c_state = -1
            cnt += 1
        else:
            continue
        if c_state != state:
            if cnt != 1:
                ans += 1
                cnt = 0
            state = c_state
    print(ans)


if __name__ == '__main__':
    main()
