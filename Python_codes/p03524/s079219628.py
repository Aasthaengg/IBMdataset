import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    cnt = [0, 0, 0]
    for s in S:
        if s == "a":
            cnt[0] += 1
        elif s == "b":
            cnt[1] += 1
        else:
            cnt[2] += 1
    if max(cnt) - min(cnt) > 1:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
