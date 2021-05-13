p = input()

s = list(p)
s.sort()

answer = -1

check = []
for i in range(26):
    check.append(False)

for i in range(len(s)):
    x = ord(s[i])
    check[x - 97] = True

for i in range(26):
    if not check[i]:
        answer = i + 97
        break

if answer == -1:
    print('None')
else:
    print(chr(answer))