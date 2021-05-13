import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())

    def main(N):
        i = 1
        ans = 0

        while True:
            ans += i
            if ans >= N:
                print(i)
                if N - i != 0:
                    if N-i<i:
                        print(N - i)
                        return True
                    else:
                        main(N-i)
                        return True
                else:
                    return True
            else:
                i += 1

    main(N)


resolve()