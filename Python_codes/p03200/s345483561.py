s = input()

ans = 0
for i in range(len(s)):
  if s[i] == "W":
    ans += i

a = 0
for i in range(s.count("W")):
  a += i

print(ans - a)