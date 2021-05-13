s = input()
wb = s[0]
c = 0
for i in range(1, len(s)):
    if s[i] == wb:
        continue
    else:
        c += 1
        wb = s[i]

print(c)
