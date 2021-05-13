import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    S = ns()
    ans = 0
    for i in range(1, n - 1):
        X = S[:i]
        Y = S[i:]
        tmp = len(set(X) & set(Y))
        ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
