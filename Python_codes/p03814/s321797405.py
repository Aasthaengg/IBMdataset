s = input()
l = len(s)
for i in range(l):
    if s[i] == 'A':
        a = i
        break
for i in range(l - 1, -1, -1):
    if s[i] == 'Z':
        z = i
        break
print(z - a + 1)