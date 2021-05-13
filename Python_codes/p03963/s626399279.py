import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, K = map(int, readline().split())
    ans = K*((K-1)**(N-1))
    print(ans)


if __name__ == '__main__':
    main()