import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, H, W = map(int, readline().split())
    ans = 0
    for _ in range(N):
        A, B = map(int, readline().split())
        if H<=A and W<=B:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
