s = str(input())
z = 'Yes'
for i in range(len(s)):
    if i%2 == 0:
        if s[i] != 'R' and s[i] != 'U' and s[i] != 'D':
            z = 'No'
            break
    else:
        if s[i] != 'L' and s[i] != 'U' and s[i] != 'D':
            z = 'No'
            break
print(z)