MOD = 10 ** 9 + 7
cnt = [1 for _ in range(26)]
n = int(input())
string = input()
for s in string:
    cnt[ord(s) - 97] += 1
ans = 1
for num in cnt:
    ans *= num
    ans %= MOD
print((ans - 1) % MOD)