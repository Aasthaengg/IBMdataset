import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = input()
    ans = 1000
    for i in range(len(S) - 2):
        s = int(S[i:i + 3])
        ans = min(ans, (abs(s - 753)))
    print(ans)


if __name__ == '__main__':
    main()
