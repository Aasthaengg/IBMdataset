tmp = input()
data = input()
r = 0
b = 0
for i in data:
    if i == 'R':
        r += 1
    else:
        b += 1
if r > b:
    print('Yes')
else:
    print('No')