import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    s = str(readline().rstrip().decode('utf-8'))
    if s[-1] == "1":
        print(-1)
    else:
        now = n
        ans = []
        while True:
            b = False
            for j in range(now - m, now):
                if 0 <= j < n:
                    if s[j] != "1":
                        b = True
                        ans.append(now - j)
                        now = j
                        if j == 0:
                            ans.reverse()
                            print(*ans)
                            exit()
                        break
            if not b:
                print(-1)
                exit()


if __name__ == '__main__':
    solve()
