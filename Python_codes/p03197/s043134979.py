n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)
b = True
for i in range(n):
    if l[i] % 2 != 0:
        b = False
if b:
    print('second')
else:
    print('first')