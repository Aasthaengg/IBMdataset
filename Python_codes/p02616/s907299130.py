from heapq import heapify, heappush, heappop
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,K = map(int, readline().split())
    A = [int(i) for i in readline().split()]

    MOD = 10**9+7
    ans = 1
    if K == N:
        for a in A:
            ans *= a
            ans %= MOD
        print(ans)
        exit()

    plus = []
    minus = []

    for a in A:
        if a < 0:
            heappush(minus, a)
        else:
            heappush(plus, -a)

    if not plus:
        if K % 2 == 1:
            for _ in range(N-K):
                heappop(minus)
            for _ in range(K):
                ans *= heappop(minus)
                ans %= MOD
        else:
            for _ in range(K):
                ans *= heappop(minus)
                ans %= MOD
        print(ans)
        exit()

    p = []
    m = []
    for _ in range(K):
        if plus and minus:
            if plus[0] <= minus[0]:
                p.append(-heappop(plus))
            else:
                m.append(heappop(minus))
        elif plus:
            p.append(-heappop(plus))
        else:
            m.append(heappop(minus))

    for i in p:
        ans *= i
        ans %= MOD
    for j in m:
        ans *= j
        ans %= MOD

    if len(m) % 2 == 0:
        print(ans)

    else:
        if plus and minus and p and m:
            if p[-1] * (-plus[0]) >= m[-1] * minus[0]:
                ans *= pow(m[-1], MOD-2, MOD)
                ans *= -plus[0]
                ans %= MOD
            else:
                ans *= pow(p[-1], MOD-2, MOD)
                ans *= minus[0]
                ans %= MOD
        elif plus:
            ans *= pow(m[-1], MOD-2, MOD)
            ans *= -plus[0]
            ans %= MOD
        else:
            ans *= pow(p[-1], MOD-2, MOD)
            ans *= minus[0]
            ans %= MOD
        
        print(ans)


if __name__ == "__main__":
    main()
