s = input()
for i in range(len(s)):
    if s[i] == "A":
        l = i
        break
for i in range(len(s)-1, -1, -1):
    if s[i] == "Z":
        r = i
        break
print(r-l+1)