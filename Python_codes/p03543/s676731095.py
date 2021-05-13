N = str(input())
a = N[:3]
b = N[1:]

if len(set(a)) == 1 or len(set(b)) == 1:
    print('Yes')
else:
    print('No')

