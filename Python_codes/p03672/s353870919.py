s = input()

for l in range(len(s) - 2, 0, -2):
    s = s[0:l]
    if s[0:l // 2] == s[l // 2:l]:
        break
print(l)
