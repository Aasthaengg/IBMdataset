s = input()
check = True
for c in s:
    if s.count(c) > 1:
        check = False
        break
print('yes' if check else 'no')
