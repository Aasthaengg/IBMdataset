n = int(input())
s = input()
mod = 10**9+7

s = sorted(s)
s += '#'
count = 1
ans = 1
for i in range(1, n+1):
    if s[i] == s[i-1]:
        count += 1
    else:
        ans = (ans * (count+1)) % mod
        count = 1
print(ans-1)
