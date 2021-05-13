#AGC031 A Colorful Subsequence
# Answer
N = int(input())
S = input()
alpha = [0]*26
mod = 10**9+7

for n in S:
    num = ord(n)-97
    alpha[num] += 1
    
ans = 1
for i in range(26):
    ans *= (alpha[i]+1)

# ans %= mod
print((ans-1)%mod)