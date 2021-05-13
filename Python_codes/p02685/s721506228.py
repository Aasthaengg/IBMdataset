N, M, K = map(int, input().split())
kMod = 998244353

# [100, 0, 0]                                                                                                                                                                                                                                 
# [100, 9900, 0]                                                                                                                                                                                                                              
# [100, 19800, 9900*99]                                                                                                                                                                                                                       

# M, M*(M-1)*C(N-1, 1),M*(M-1)^2*C(N-1, 2),M*(M-1)^3*C(N-1,3)                                                                                                                                                                                 

ans = 0
for i in range(N):
    if i == 0:
        acc = M
    else:
        acc *= (M-1)
        acc %= kMod
        acc *= (N-i)
        acc %= kMod
        acc *= pow(i, kMod-2, kMod)
        acc %= kMod
    if i >= N-K-1:
        ans += acc
        ans %= kMod
print(ans)

