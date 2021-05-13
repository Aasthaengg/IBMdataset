s = input()
for i in range(len(s)):
    if s[i] == "A":
        start = i
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] == "Z":
        end = i
        break
print(len(s[start:end + 1]))
