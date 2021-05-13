a = list(input())
s = list('CODEFESTIVAL2016')
b = 0
x = -1
dx = -1
while 1:
    x += 1
    dx += 1
    if x == len(a):
        break
    elif a[x] != s[dx]:
        b += 1
print(b)