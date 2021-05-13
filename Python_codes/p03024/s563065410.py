s = input()
n = 0
m = 15 - len(s)

for i in range(len(s)):
    if s[i] == "o":
        n += 1

if n + m >= 8:
    print("YES")
else:
    print("NO")
