s = input()

for i in range(26):
    x = chr(i + 97)
    if not x in s:
        print(x)
        exit()
print('None')
