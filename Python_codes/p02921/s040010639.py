s = input().rstrip()
t = input().rstrip()
r = 0
for i in range(len(s)):
    if s[i] == t[i]:
        r = r + 1

print(r)
