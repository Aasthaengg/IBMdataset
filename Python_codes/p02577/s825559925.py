s = input()
x = 0
for i in s:
    x += int(i)
if x%9:
    print('No')
else:
    print('Yes')
