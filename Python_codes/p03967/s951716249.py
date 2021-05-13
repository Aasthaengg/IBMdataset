s = input()

c = 0

for i in range(len(s)):
    if s[i]=='g':
        c = c+1

print(len(s)//2-(len(s)-c))