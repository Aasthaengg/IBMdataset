l = input()
n = len(l)
mod = 1000000007
ans = 0
cnt = 0
for i in range(n):
    if l[i] == "1":
        ans += pow(3, n - i - 1, mod) * pow(2, cnt, mod)
        ans %= mod
        cnt += 1
ans += pow(2, cnt, mod)
ans %= mod
print(ans)