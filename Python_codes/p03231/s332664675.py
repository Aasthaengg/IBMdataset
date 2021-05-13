import sys
import fractions

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    S = input().strip()
    T = input().strip()

    ans = (N * M) // fractions.gcd(N, M)

    dic = {}
    for i, s in enumerate(S):
        dic[(ans // N) * i + 1] = s

    for i, t in enumerate(T):
        if ((ans // M) * i + 1) in dic.keys():
            if dic[(ans // M) * i + 1] != t:
                print(-1)
                return

    print(ans)


if __name__ == '__main__':
    main()
