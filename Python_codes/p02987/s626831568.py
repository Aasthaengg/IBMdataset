s = input()
v = [0] * 26
for i in range(4):
    v[ord(s[i])-65] += 1
for i in range(26):
    if v[i] == 1 or v[i] == 3 or v[i] == 4:
        print('No')
        exit()
print('Yes')