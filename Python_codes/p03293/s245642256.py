s = input()
t = input()

for i in range(len(s)-1, -1, -1):
    rotated = s[i:] + s[:i]
    if rotated == t:
        print('Yes')
        exit()
print('No')