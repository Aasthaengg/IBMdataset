s = input()
for i in range(len(s)):
    if s[i] == 'A':
        Ai = i
        break
for i in range(len(s))[::-1]:
    if s[i] == 'Z':
        Zi = i
        break
print(Zi-Ai+1)
