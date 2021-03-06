

# def main():
#     n = int(input())
#     al = list(map(int, input().split()))
#     all_xor = 0
#     for a in al:
#         all_xor = all_xor ^ a

#     ans = []
#     for a in al:
#         curr_ans = all_xor ^ a
#         ans.append(curr_ans)

#     print(*ans)


# if __name__ == "__main__":
#     main()


N_MAX = 2*(10**6)
MOD = 10**9 + 7
fac, finv, inv = [0]*N_MAX ,[0]*N_MAX, [0]*N_MAX
def com_init():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, N_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def com(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def main():
    k = int(input())
    s = input()
    n = len(s)

    com_init()

    ans = 0
    for i in range(0,k+1):
        ans += (pow(25,k-i,MOD) * pow(26,i,MOD))*com(n+k-i-1,n-1)

    print(ans%MOD)


if __name__ == "__main__":
    main()