s = list(input())

for i in range(len(s)):
    if s[i] == "?":
        s[i] = "D"
s = "".join(s)
print(s)