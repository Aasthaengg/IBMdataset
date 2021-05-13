n = int(input())
s = input()
mod = 10**9 + 7

cnt = [0] * 26
for i in range(26):
    cnt[i] = s.count(chr(i+97)) + 1

ans = 1
for i in cnt:
    ans *= i
    ans %= mod

ans -= 1
ans %= mod
print(ans)