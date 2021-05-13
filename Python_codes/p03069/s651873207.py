import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    S = list(input())
    numb = 0
    numw = S.count(".")
    answer = numb + numw
    for i in range(N):
        if S[i] == "#":
            numb += 1
        else:
            numw -= 1
        if answer > numb + numw:
            answer = numb + numw

    print(answer)


if __name__ == "__main__":
    main()
