s = input()
for i in s:
    if s.count(i) != 1:
        print('no')
        exit()
print('yes')