import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


N = int(readline())
B = list(map(int, readline().split()))


def main():
    ans = []
    while B:
        found = False
        for i in range(len(B), 0, -1):
            if i == B[i - 1]:
                ans.append(i)
                del B[i - 1]
                found = True
                break
        if not found:
            print(-1)
            return
    print(*reversed(ans), sep='\n')


if __name__ == '__main__':
    main()
