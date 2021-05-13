import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    if N == K:
        ans = 1
        for a in A:
            ans *= a
            ans %= MOD
        print(ans)
        return
    
    if all(a < 0 for a in A) and K%2 == 1:
        A.sort(reverse = True)
        ans = 1
        for i in range(K):
            ans *= A[i]
            ans %= MOD
        print(ans)
        return
    
    A.sort(key = abs,reverse = True)
    cnt_m = 0
    ans = 1
    last_p = -1
    last_m = 1
    for i in range(K):
        if A[i] == 0:
            print(0)
            return
        elif A[i] < 0:
            ans *= A[i]
            ans %= MOD
            cnt_m += 1
            last_m = A[i]
        else:
            ans *= A[i]
            ans %= MOD
            last_p = A[i]
    if cnt_m%2 == 0:
        print(ans)
    else:
        diff1 = last_p
        diff2 = last_m
        inv1 = pow(last_m,MOD - 2,MOD)
        inv2 = pow(last_p,MOD - 2,MOD)
        for i in range(K,N):
            if A[i] >= 0:
                diff1 *= A[i]
                inv1 *= A[i]
                inv1 %= MOD
                break
            if i == N - 1:
                diff1 = -1
        for i in range(K,N):
            if A[i] < 0:
                diff2 *= A[i]
                inv2 *= A[i]
                inv2 %= MOD
                break
            if i == N - 1:
                diff2 = -1
        
        if last_p > 0:
            if diff1 < diff2:
                ans *= inv2
                ans %= MOD
            else:
                ans *= inv1
                ans %= MOD
        else:
            ans *= inv1
            ans %= MOD
        print(ans)
if __name__ == '__main__':
    main()