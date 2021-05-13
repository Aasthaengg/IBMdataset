s = set(list(input()))

for i in range(26):
    si = chr(i+ord('a'))
    if not si in s:
        print(si)
        exit()
print('None')

