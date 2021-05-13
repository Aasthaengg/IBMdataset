N = int(input())
A = map(int, input().split())
MOD = 10 ** 9 + 7

cnt = [0] * (N + 1)
cnt[0] = 3

ans = 1
for a in A:
    ans = (ans * cnt[a]) % MOD
    cnt[a] -= 1
    cnt[a + 1] += 1

print(ans)
