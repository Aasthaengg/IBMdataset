string = input()
s = 0
for i in string:
    s += int(i)

if s % 9 == 0:
    print('Yes')
else:
    print('No')