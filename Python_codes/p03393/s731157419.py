import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    A = set(chr(ord("a") + x) for x in range(26))
    if len(S) < 26:
        se = A - set(S)
        x = min(se)
        print(S + x)

    else:
        if S == "".join(sorted(A, reverse=True)):
            print(-1)
            return
        else:
            c = []
            S = list(S)
            while True:
                x = S[-1]
                if not c or (x > max(c)):
                    c.append(S.pop())
                    continue
                y = min(ch for ch in c if ch > x)
                S = "".join(S[:-1]) + y
                print(S)
                return


if __name__ == "__main__":
    main()
