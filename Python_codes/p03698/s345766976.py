s = str(input())
a = []
for i in s:
    if i in a:
        print('no')
        exit()
    a.append(i)
print('yes')