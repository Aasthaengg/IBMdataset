num = int(input())

for i in range(1,num + 1):
    x = str(i)
    if i % 3 == 0:
        print (end = ' ')
        print (i, end = '')
    elif '3' in x:
        print (end = ' ')
        print (i, end = '')

print()