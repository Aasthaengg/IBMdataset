import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, readline().split())
    ans = 0
    for i in range(N)[::-1]:
        if (A[i]+ans)%B[i]==0:
            continue
        else:
            ans += B[i]-(A[i]+ans)%B[i]
    print(ans)


if __name__ == '__main__':
    main()