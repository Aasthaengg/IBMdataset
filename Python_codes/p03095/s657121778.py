N = int(input())
S = input()
alpha = [0]*123
mod = 10**9+7

for n in S:
    num = ord(n)
    alpha[num] += 1
    
ans = 1
for i in range(97,123):
    ans *= (alpha[i]+1)%mod

ans -= 1
ans %= mod
print(ans)

