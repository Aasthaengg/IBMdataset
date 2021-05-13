MOD = 10**9 + 7

N = int(input())
S = input()
lis = [1] * 26
for i in range(N):
    lis[ord(S[i])-ord('a')] += 1
ans = 1
for i in range(26):
    ans *= lis[i]
    ans %= MOD
print(ans - 1)
