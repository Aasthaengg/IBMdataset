import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, L = map(int, readline().split())
    
    full = N * L + N * (N-1) // 2
    min_error = INF
    for i in range(N):
        tmp = (N-1) * L + sum(j for j in range(N) if j != i)
        if min_error > abs(full-tmp):
            min_error = abs(full-tmp)
            ans = tmp
            
    print(ans)
    return


if __name__ == '__main__':
    main()
