s = list(input())
while s:
    c = s.pop()
    if c in s:
        print('no')
        exit()
print('yes')