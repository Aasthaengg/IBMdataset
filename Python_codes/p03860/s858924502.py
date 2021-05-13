s = list(input())
print('A', end='')
for i in range(len(s)):
    if s[i] == ' ':
        print(s[i + 1], end='')
        break
print('C')
