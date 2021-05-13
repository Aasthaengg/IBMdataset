N = int(input())
S = input()

r = 0
b = 0
for si in S:
    if si == 'R':
        r += 1
    else:
        b += 1

if r > b:
    print('Yes')
else:
    print('No')