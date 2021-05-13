s = str(input())
a_index = 0
z_index = 0
for i in range(len(s)):
    if s[i] == 'A':
        a_index = i
        break
for i in range(len(s)):
    if s[i] == 'Z':
        z_index = i

print(z_index - a_index + 1)