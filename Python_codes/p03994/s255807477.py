s = list(input())
k = int(input())
#print(ord("z"))
for i in range(len(s)):
  if s[i] != 'a' and 123 - ord(s[i]) <= k:
    k -= (123 - ord(s[i]))
    s[i] = "a"
    #print(k)
#print(s, k)
k %= 26
if ord(s[-1]) + k > 122:
  s[-1] = chr(ord(s[-1]) + k - 26)
else:
  s[-1] = chr(ord(s[-1]) + k)
ans = ""
for i in s:
  ans += i
print(ans)