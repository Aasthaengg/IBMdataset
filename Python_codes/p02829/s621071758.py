import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A = int(input())
    B = int(input())
    ans = [1, 2, 3]
    ans.remove(A)
    ans.remove(B)
    print(ans[0])


if __name__ == '__main__':
    solve()
