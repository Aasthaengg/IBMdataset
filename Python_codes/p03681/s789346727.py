import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, M = map(int, readline().split())
    if abs(N-M)>1:
        print('0')
    elif N==M:
        fact=[1]*(N+1)
        for i in range(N):
            fact[i+1] = fact[i]*(i+1)%MOD
        ans = 2*fact[N]*fact[M]%MOD
        print(ans)
    else:
        fact = [1] * (N + 3)
        for i in range(N+2):
            fact[i + 1] = fact[i] * (i + 1)%MOD
        ans = fact[N] * fact[M]%MOD
        print(ans)
if __name__ == '__main__':
    main()