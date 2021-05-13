n = input()
x = list(n)
a = 0
for i in x :
    a += int(i)
if a%9 == 0 :
    print('Yes')
else :
    print('No')