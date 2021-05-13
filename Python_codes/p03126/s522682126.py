import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m = nm()
    cnt = [0] * m
    for i in range(n):
        k, *A = nm()
        for a in A:
            cnt[a - 1] += 1
    print(cnt.count(n))


if __name__ == '__main__':
    main()
