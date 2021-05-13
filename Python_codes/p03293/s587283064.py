import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = ns()
    T = ns()
    for i in range(len(T)):
        if S == T[i:] + T[:i]:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
