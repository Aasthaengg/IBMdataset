a = input()
b = a.split(' ')
c = int(b[0])
d = int(b[1])
e = int(b[2])
if c < d < e:
    print('Yes')
else:
    print('No')