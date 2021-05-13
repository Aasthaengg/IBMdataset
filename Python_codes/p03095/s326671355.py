n = int(input())
s = input()
mod = 10**9 + 7

ans = 0
cnt = [1] * 26
for i,ch in enumerate(s):
    tmp = 1
    for j in range(26):
        if(j==(ord(ch) - 97)):
            continue
        tmp *= cnt[j]
        tmp %= mod
    ans += tmp
    ans %= mod
    cnt[ord(ch) - 97] += 1

print(ans)