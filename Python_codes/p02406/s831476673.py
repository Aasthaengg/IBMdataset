num = int(input())

for i in range(1,num + 1):
    x = str(i)
    if i % 3 == 0 or '3' in x:
        print (end = ' ')
        print (i, end = '')

print()