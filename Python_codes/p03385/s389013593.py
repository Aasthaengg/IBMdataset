s = str(input())
a = ['a', 'b', 'c']
for i in s:
    if i not in a:
        print('No')
        exit()
    else:
        a.remove(i)
print('Yes')