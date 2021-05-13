import sys
s = list(input())

i = 0
for e in s:
    if i % 2 == 0 and e == 'L':
        print('No')
        sys.exit()
    elif i % 2 == 1 and e == 'R':
        print('No')
        sys.exit()
    i += 1

print('Yes')
