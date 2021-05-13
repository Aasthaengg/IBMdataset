x = input()
y = x.split(' ')
a = int(y[0])
b = int(y[1])
d = a//b
r = a%b
f = a/b
print('%s %s %s' % (d,r,'%03.8f'%f))