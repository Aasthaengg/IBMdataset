import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    X = input()
    answer = len(X)
    cnt_s = 0
    for x in X:
        if x == "S":
            cnt_s += 1
            continue
        if cnt_s > 0:
            cnt_s -= 1
            answer -= 2
            
    print(answer)


if __name__ == "__main__":
    main()
