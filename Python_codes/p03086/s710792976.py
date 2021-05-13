import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = input()
    ans = 0
    tmp = 0
    acgt = ['A', 'C', 'G', 'T']
    for s in S:
        if s in acgt:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
