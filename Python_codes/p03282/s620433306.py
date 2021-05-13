import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    K = int(input())

    i = 0

    for i in range(K):
        if S[i]=="1":
            continue
        else:
            print(S[i])
            exit()
    print(1)


if __name__ == "__main__":
    main()
