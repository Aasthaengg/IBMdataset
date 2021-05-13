s = input()
l = -1
r = -1
for i in range(len(s)):
    if s[i] == 'A' and l == -1:
        l = i
    elif s[i] == 'Z':
        r = i
print(r-l+1)