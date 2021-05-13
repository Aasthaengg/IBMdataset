s = input()
mae = s[0]
cou = 0
for i in range(len(s)):
    if s[i] != mae:
        cou += 1
        mae = s[i]
print(cou)