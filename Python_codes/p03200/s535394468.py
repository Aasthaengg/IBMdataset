s = input()

b = 0
c = 0
for i in range(len(s)):
    if s[i] == "B":
        b += 1
    else:
        c += b

print(c)