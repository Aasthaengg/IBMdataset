import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, M, K = map(int, input().split())
    for i in range(N+1):
        for j in range(M+1):
            S = (M-j)*(N-i)+i*j
            if S == K:
                print('Yes')
                break
        else:
            continue
        break
    else:
        print('No')

if __name__ == '__main__':
    main()
