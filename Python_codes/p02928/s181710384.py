import sys
import bisect

MOD = pow(10, 9)+7
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    init = []
    for i in range(N):
        cnt = 0
        for j in range(0, i):
            if A[j] < A[i]:
                cnt += 1
        init.append(cnt)
    
    Atmp = A.copy()
    Atmp.sort()
    large = []
    for i in range(N):
        large.append(bisect.bisect_left(Atmp, A[i]))

    ans = 0
    for i in range(N):
        a0 = large[i]*K-init[i]
        b = large[i]
        ans += K*a0 - ((K*(K-1))//2)*large[i]
        ans %= MOD
    print(ans%MOD)

if __name__ == "__main__":
    main()
