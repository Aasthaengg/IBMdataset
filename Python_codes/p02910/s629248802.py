s = input()
n = len(s)

for i in range(0, n, 2):
    if s[i] == 'L':
        print('No')
        exit()

for i in range(1, n, 2):
    if s[i] == 'R':
        print('No')
        exit()

print('Yes')
