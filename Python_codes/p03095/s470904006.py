n = int(input())
s = input()
mod = 10 ** 9 + 7
cnt = [0] * 26  # それぞれの文字に対してfreqを数える
for i in s:
    cnt[ord(i) - 97] += 1
ans = 1
for i in cnt:
    ans *= i + 1
    ans %= mod
print(ans - 1)
