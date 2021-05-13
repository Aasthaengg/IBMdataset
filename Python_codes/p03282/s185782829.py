import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = list(map(int, (list(ns()))))
    K = ni()
    for i in range(K):
        if S[i] != 1:
            print(S[i])
            return
    print(1)


if __name__ == '__main__':
    main()
