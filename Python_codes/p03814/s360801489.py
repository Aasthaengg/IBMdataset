s = input()

left = 0
right = 0
for i in range(len(s)):
    if s[i] == 'A':
        left = i
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] == 'Z':
        right = i
        break
print(right - left + 1)