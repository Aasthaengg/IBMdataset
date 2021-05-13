n = int(input())
s = str(input())

x = 0
m = 0
for i in s:
    if i == 'I':
        x += 1
    else:
        x -= 1
    if m < x:
        m = x
print(m)