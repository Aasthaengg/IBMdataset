s = input()
for i in range(26):
    if s.count(chr(ord('a')+i)):
        continue
    else:
        print(chr(ord('a')+i))
        exit()
print('None')