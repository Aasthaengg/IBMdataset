import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N = int(input())
    sum = 0
    for i in range(1, N + 2):
        if sum < N:
            sum += i
        else:
            S = i
            break
    a = sum - N
    for j in range(1, S):
        if j == a:
            continue
        else:
            print(j)


if __name__ == "__main__":
    main()
