MOD = 10 ** 9 + 7

n = int(input())
alst = list(map(int, input().split()))
bin_s = [2 ** i for i in range(60)]
cnt = [0 for _ in range(60)]

for a in alst:
    for j in range(60):
        if bin_s[j] & a:
            cnt[j] += 1

ans = 0
for i in range(60):
    ans += bin_s[i] * cnt[i] * (n - cnt[i])
    ans %= MOD
print(ans)