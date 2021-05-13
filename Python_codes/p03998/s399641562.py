a = list(input())
b = list(input())
c = list(input())

s = a.pop(0)
for i in range(400):
    if s == 'a':
        if a == []:
            break
        s = a.pop(0)
    elif s == 'b':
        if b == []:
            break
        s = b.pop(0)
    elif s == 'c':
        if c == []:
            break
        s = c.pop(0)
print(s.upper())