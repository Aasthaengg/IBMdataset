str = raw_input()
a0, b0 = str.split()
a = int(a0)
b = int(b0)

if a<b:
    print 'a < b'
elif a>b:
    print 'a > b'
else:
    print 'a == b'