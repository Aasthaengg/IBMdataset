a = input()
b = input()
if len(a) > len(b):
    print('GREATER')
    exit()
if len(a) < len(b):
    print('LESS')
    exit()
for i in range(len(a)):
    if a[i] > b[i]:
        print('GREATER')
        exit()
    if a[i] < b[i]:
        print('LESS')
        exit()
print('EQUAL')