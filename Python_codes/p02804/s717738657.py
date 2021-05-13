import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,K = LI()
    A = LI()

    f = [1]
    r = [1]
    c = 1
    for i in range(1,N+1):
        c = (c * i) % MOD
        f.append(c)
        r.append(pow(c,MOD-2,MOD))

    def comb(n,k):
        return f[n] * r[k] * r[n-k]

    A.sort()
    max_a = 0
    min_a = 0
    for i in range(N-1,K-2,-1):
        max_a = (max_a + A[i] * comb(i,K-1)) % MOD
    for i in range(N-K+1):
        min_a = (min_a + A[i] * comb(N-1-i,K-1)) % MOD
    print((max_a - min_a) % MOD)

if __name__ == '__main__':
    main()