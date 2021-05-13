n = int(input())
S = [ord(t) - ord('a') for t in input()]
cnt = [0]*26
for s in S:
    cnt[s] += 1
ans = 1
mod = 10**9 + 7
for c in cnt:
    ans *= c+1
    ans %= mod
print((ans-1)%mod)
