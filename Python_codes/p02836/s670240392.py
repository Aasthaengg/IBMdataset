s = input()
ans = 0
center = len(s) // 2

if len(s) % 2 == 1:
  s2 = s[center+1:]
else:
  s2 = s[center:]

s1 = s[:center]
s2 = "".join(reversed(s2))
for str1 , str2 in zip(s1,s2):
  if str1 != str2:
    ans += 1
print(ans)