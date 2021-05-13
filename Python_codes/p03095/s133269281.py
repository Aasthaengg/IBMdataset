N = int(input())
S = list(input())
mod = 10**9+7
ans = 1
for i in 'abcdefghijklmnopqrstuvwxyz':
    ans *= S.count(i)+1
    ans %= mod
print((ans-1) % mod)