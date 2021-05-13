N = int(input())
mod = 10**9+7
memo = {}

for i in range(2, N+1):
    for j in range(2, i+1):
        while i % j == 0:
            i  = i // j
            try:
                memo[j] += 1
            except:
                memo[j] = 1

ans = 1
for key in memo.keys():
    ans *= memo[key] + 1

print(ans%mod)
