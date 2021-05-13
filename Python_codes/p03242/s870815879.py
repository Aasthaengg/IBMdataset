n = str(input())
a = ''
for i in n:
    if i == '1':
        a += '9'
    else:
        a += '1'
print(int(a))