S = input()
n = len(S)
up = 0
flag = False

for i, s in enumerate(S):
    if (i == 0) & (s != 'A'):
        break
    if s.isupper():
        up += 1
    if (1 < i) & (i < n-1):
        if s == 'C':
            flag = True

if flag & (up == 2):
    print('AC')
else:
    print('WA')

