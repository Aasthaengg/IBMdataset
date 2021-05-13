x, y = map(int, input().split())
xgroup = ''
ygroup = ''
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
for i in a:
    if x == i:
        xgroup = 'a'
for i in a:
    if y == i:
        ygroup = 'a'
for i in b:
    if x == i:
        xgroup = 'b'
for i in b:
    if y == i:
        ygroup = 'b'
for i in c:
    if x == i:
        xgroup = 'c'
for i in c:
    if y == i:
        ygroup = 'c'
if xgroup == ygroup:
    print('Yes')
else:
    print('No')
