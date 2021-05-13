import sys
from bisect import bisect_left, bisect_right


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, q = nm()
    S = input()
    ans = []
    A_pos = []
    C_pos = []
    for i in range(n - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            A_pos += [i + 1]
            C_pos += [i + 2]
    for i in range(q):
        l, r = nm()
        ans += [bisect_right(C_pos, r) - bisect_left(A_pos, l)]
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
