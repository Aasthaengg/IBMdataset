import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())

    if K > (N - 1) * (N - 2) // 2:
        print('-1')
        return
        
    m = (N - 1) * (N - 2) // 2 - K
    M = N - 1 + m
    
    print(M)
    for i in range(2, N+1):
        print(1, i)
    
    i, j = 2, 3
    for _ in range(m):
        print(i, j)
        if j == N:
            i += 1
            j = i + 1
        else:
            j += 1

    return


if __name__ == '__main__':
    main()
