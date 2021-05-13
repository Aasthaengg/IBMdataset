s = list(set((input())))

s.sort()

for i in range(26):
    if i >= len(s) or s[i] != chr(i + ord('a')):
        print(chr(i + ord('a')))
        exit()
else:
    print('None')