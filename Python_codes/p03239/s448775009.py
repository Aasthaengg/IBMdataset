import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')


def main():
    N, T = map(int, readline().split())
    ans = INF

    for _ in range(N):
        c, t = map(int, readline().split())
        if t<=T:
            ans = min(ans, c)

    if ans == INF:
        print('TLE')
    else:
        print(ans)
if __name__ == '__main__':
    main()
