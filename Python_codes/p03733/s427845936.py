import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, T = map(int, readline().split())
    t = list(map(int, readline().split()))
    ans = T
    for i in range(N-1):
        ans += min(T, t[i+1]- t[i])
    print(ans)
if __name__ == '__main__':
    main()