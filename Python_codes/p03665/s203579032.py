from collections import Counter

MOD = 10**9+7
MAX_N = 50
inv = [0] * (MAX_N+1)
finv = [0] * (MAX_N+1)
fac = [0] * (MAX_N+1)
inv[1] = 1
finv[0] = 1; finv[1] = 1
fac[0] = 1; fac[1] = 1

def COM_init():
    for i in range(2, MAX_N+1):
        inv[i] = -(MOD//i)*inv[MOD%i]%MOD
        finv[i] = finv[i-1]*inv[i]%MOD
        fac[i] = fac[i-1]*i%MOD

def COM(a, b):
    if a < 0 or b < 0:return 0
    if a < b:return 0
    
    return fac[a]*finv[a-b]*finv[b]%MOD

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = [a%2 for a in A]
    c = Counter(B)
    
    n0 = c[0]
    n1 = c[1]
    ans = 0
    COM_init()
    for i in range(P, n1+1, 2):
        ans += pow(2, n0) * COM(n1, i)

    print(ans) 
         

if __name__ == "__main__":
    main()