import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    K = int(input())
    last = ""
    a = 0
    A = set(list(S))
    if len(S) == 1:
        print(K // 2)
        return

    elif len(A) == 1:
        if len(S) % 2 == 1:
            a = K % 2
            print(len(S) * (K // 2) + (len(S) // 2) * a)
        else:
            a = K % 2
            print(len(S) * (K // 2) + (len(S) // 2) * a)
    else:
        for s in S:
            if s == last:
                a += 1
                last = ""
            else:
                last = s
        if S[0] != S[-1]:
            print(a * K)
        elif len(S) == 2:
            print(a * K)
        else:
            x = 0
            y = 0
            for i in range(len(S) // 2):
                if S[i] == S[0]:
                    x += 1
            for j in range(len(S) // 2):
                if S[len(S) - j - 1] == S[-1]:
                    y += 1

            if x % 2 == 1 and y % 2 == 1:
                b = 1
            else:
                b = 0

            print(a * K + b * (K - 1))


if __name__ == "__main__":
    main()
