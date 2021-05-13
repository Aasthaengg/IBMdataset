s = input()
k = int(input())
a = ord("a") + 26
mod = 26
ans = ""
for i in s[:-1]:
  tmp = (a - ord(i)) % mod
  if tmp <= k:
    k -= tmp
    ans += "a"
  else:
    ans += i
ans += chr(ord("a") + (ord(s[-1]) - a + k) % mod)
print(ans)