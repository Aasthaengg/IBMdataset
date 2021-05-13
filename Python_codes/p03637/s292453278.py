N,*a = map(int, open(0).read().split())
b = [x for x in a if x % 4 == 0]
c = [x for x in a if x % 2 == 0]
d = [x for x in a if x % 2 == 1]
if len(b) >= len(a) // 2:
    print('Yes')
elif len(d) <= len(b):
    print('Yes')
elif len(c) == len(a):
    print('Yes')
else:
    print('No')