import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *P = map(int, read().split())
    
    if P == sorted(P):
        print('YES')
        return
    
    for i in range(N-1):
        for j in range(i+1, N):
            B = P[:]
            B[i] = P[j]
            B[j] = P[i]
            if B == sorted(P):
                print('YES')
                return
                
    print('NO')
    return


if __name__ == '__main__':
    main()
