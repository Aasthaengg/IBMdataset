s = str.upper(input())

for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break


for i in range(1,len(s)):
    if s[-i] == 'Z':
        b = len(s) + 1 - i
        break
print(b-a)