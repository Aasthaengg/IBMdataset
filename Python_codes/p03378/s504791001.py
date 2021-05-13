import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m, x = nm()
    A = nl()
    cost = [0] * 101
    for a in A:
        cost[a] = 1
    ans_1 = 0
    ans_2 = 0
    for i in range(x):
        ans_1 += cost[i]
    for i in range(x, n + 1):
        ans_2 += cost[i]
    print(min(ans_1, ans_2))


if __name__ == '__main__':
    main()
