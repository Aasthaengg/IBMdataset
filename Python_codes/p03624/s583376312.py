s = list(str(input()))
l = set(s)
for i in range(26):
    c = chr(ord('a')+i)
    if c not in l:
        print(c)
        exit()
else:
    print('None')
