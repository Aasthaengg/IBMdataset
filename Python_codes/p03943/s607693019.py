a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a == b + c or b == a + c or c == a + b:
    print('Yes')
else:
    print('No')