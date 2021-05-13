from sys import exit

N = int(input())
s = input()

r = 0
b = 0

for si in s:
    if si == 'R':
        r += 1
    else:
        b += 1

if r > b:
    print('Yes')
else:
    print('No')
