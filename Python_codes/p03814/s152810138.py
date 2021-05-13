s = input()
for i in range(len(s)):
    if s[i] == 'A':
        b = i
        break
for i in range(len(s)-1, 0, -1):
    if s[i] == 'Z':
        e = i
        break
print(e - b + 1)