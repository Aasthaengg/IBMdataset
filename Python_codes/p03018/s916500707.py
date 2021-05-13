import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    S = S.replace("BC", "X")
    cnt_a = 0
    answer = 0
    for s in S:
        if s == "A":
            cnt_a += 1
        elif s == "X":
            answer += cnt_a
        else:
            cnt_a = 0
    print(answer)


if __name__ == "__main__":
    main()
