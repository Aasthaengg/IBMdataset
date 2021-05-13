s = list(input())

for i in range(len(s)):
    if s[i] == ',':
        s[i] = ' '
    
print(''.join(s))