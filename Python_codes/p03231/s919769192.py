def main():
    import sys
    from collections import defaultdict
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    N, M = [int(x) for x in input().strip().split()]
    S = input().strip()
    T = input().strip()
    L = (N * M) // gcd(N, M)
    d = defaultdict(int)
    for n in range(N):
        d[L//N*n] = S[n]
    for m in range(M):
        if d[L//M*m] == 0 or d[L//M*m] == T[m]:
            continue
        else:
            print(-1)
            return
    print(L)

if __name__ == '__main__':
    main()