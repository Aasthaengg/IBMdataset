import sys
import collections


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    ls = []
    for i in range(3):
        a, b = list(map(int, input().rstrip('\n').split()))
        ls.append(a)
        ls.append(b)
    ls = collections.Counter(ls).most_common()
    print("YES" if ls[0][1] == 2 and ls[1][1] == 2 and ls[2][1] == 1 and ls[3][1] == 1 else "NO")


if __name__ == '__main__':
    solve()
