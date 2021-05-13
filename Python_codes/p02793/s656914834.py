#coding:utf-8
import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    # def gen_primes2(upper_bound):
    #     upper_bound += 1
    #     P = [True] * upper_bound
    #     P[0] = P[1] = False
    #     for i in range(4,upper_bound,2):
    #         P[i] = False
    #     for i in range(3,int(upper_bound**0.5),2):
    #         if P[i]:
    #             for j in range(i**2,upper_bound,i):
    #                 P[j] = False
    #     res = []
    #     for i in range(upper_bound):
    #         if P[i]:
    #             res.append(i)
    #     return res

    N = II()
    A = LMIIS()
    # upper_bound = max(A)
    # primes = gen_primes2(upper_bound)
    # LCMP = [0]*len(primes)
    # for i in range(N):
    #     # if i % 100 == 0:
    #     #     print(i)
    #     a = A[i]
    #     for j,p  in enumerate(primes):
    #         t = 0
    #         while a % p == 0:
    #             a //= p
    #             t += 1
    #         LCMP[j] = max(t, LCMP[j])
    #         if a == 1:
    #             break
    # lcm = 1
    # for i in range(len(primes)):
    #     lcm = lcm * pow(primes[i],LCMP[i],MOD) % MOD
    lcm = A[0]
    from fractions import gcd

    for i in range(1,N):
        lcm = lcm * A[i] // gcd(lcm,A[i])

    invans = 0
    for a in A:
        invans += pow(a, MOD-2, MOD)
        invans %= MOD
    print(lcm*invans%MOD)

if __name__ == '__main__':
    main()