import sys


def input():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(100000)


def main():
    n, h = [int(i) for i in input().strip().split()]
    attack = []
    throw = []
    for _ in range(n):
        a, t = [int(i) for i in input().strip().split()]
        attack.append(a)
        throw.append(t)

    a_max = max(attack)
    throw = sorted(throw)[::-1]
    cnt = 0
    for t in throw:
        if t > a_max:
            h -= t
            cnt += 1
        elif t <= a_max:
            break
        if h <= 0:
            print(cnt)
            return
    if h > 0:
        cnt += h // a_max
        if h % a_max > 0:
            cnt += 1
    print(cnt)

    return


if __name__ == "__main__":
    main()
